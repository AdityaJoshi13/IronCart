import razorpay
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import db, User, Product, CartItem
from dotenv import load_dotenv
import os


app = Flask(__name__)
app.config.from_object(Config)

load_dotenv()

# Initialize Extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# --- RAZORPAY CONFIGURATION ---
# Replace these with your actual Test Keys from Razorpay Dashboard
razorpay_client = razorpay.Client(auth=(
    os.getenv("RAZORPAY_KEY_ID"),
    os.getenv("RAZORPAY_KEY_SECRET")
))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- DATABASE SEEDER (Runs automatically) ---
def seed_database():
    # 1. Create Default Admin if not exists
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        hashed_pw = generate_password_hash('admin123')
        # Create admin user with is_admin=True
        admin = User(username='admin', password=hashed_pw, is_admin=True) 
        db.session.add(admin)
        print("SUPERUSER CREATED: admin / admin123")
    
    # 2. Create Products if the table is empty
    if not Product.query.first(): 
        products = [
            ("Obsidian Dumbbells (20kg)", 3500, "dumbbells.jpg", "Matte black finish. Hex design."),
            ("Phantom Treadmill", 25000, "treadmill.jpg", "Silent motor technology. Bluetooth enabled."),
            ("Void Whey Protein", 4500, "whey.jpg", "Dark Chocolate isolate. Zero sugar."),
            ("Stealth Gym Bag", 1200, "bag.jpg", "Waterproof tactical bag with shoe compartment."),
            ("Neon Grip Straps", 800, "straps.jpg", "Enhanced wrist support for heavy lifts."),
            ("Shadow Boxing Gloves", 2200, "gloves.jpg", "Pro-grade leather. Impact resistant."),
            ("Zero-G Resistance Bands", 1500, "bands.jpg", "Complete set. 5 levels of resistance."),
            ("Cyber Shaker", 600, "shaker.jpg", "Electric mixing capability. USB rechargeable."),
            ("Nightfall Yoga Mat", 1800, "mat.jpg", "Extra thick non-slip surface."),
            ("Titan Bench Press", 12000, "bench.jpg", "Adjustable incline/decline. Steel frame.")
        ]
        
        for name, price, img, desc in products:
            p = Product(name=name, price=price, image_file=img, description=desc)
            db.session.add(p)
        print("Products seeded.")
        
    db.session.commit()
    #print("Database seeded successfully.")

# --- ROUTES ---

@app.route('/')
def home():
    query = request.args.get('q')
    if query:
        products = Product.query.filter(Product.name.contains(query)).all()
    else:
        products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Check username and password.', 'danger')
            
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if User.query.filter_by(username=username).first():
        flash('Username already exists.', 'danger')
        return redirect(url_for('login'))
        
    hashed_pw = generate_password_hash(password)
    new_user = User(username=username, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    
    login_user(new_user)
    return redirect(url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        item.quantity += 1
    else:
        new_item = CartItem(user_id=current_user.id, product_id=product_id)
        db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    if request.method == 'POST':
        # Handle Razorpay success callback here if needed
        # For this example, we just clear the cart after "payment"
        CartItem.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        flash('Order Placed Successfully!', 'success')
        return redirect(url_for('home'))

    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    return render_template('cart.html', cart=cart_items, total=total, key_id=razorpay_client.auth[0])

@app.route('/delete_item/<int:item_id>')
@login_required
def delete_item(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('cart'))

@app.route('/admin')
@login_required
def admin_dashboard():
    # Security Check
    if not current_user.is_admin:
        flash('ACCESS DENIED: RESTRICTED AREA', 'danger')
        return redirect(url_for('home'))
        
    # Gather Data to Show
    users = User.query.all()
    products = Product.query.all()
    
    return render_template('admin.html', users=users, products=products)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_database()
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)