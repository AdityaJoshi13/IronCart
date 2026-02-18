// main.js - IronCart Interactive Elements

document.addEventListener('DOMContentLoaded', () => {
    
    // Add glitch effect to buttons on click
    const buttons = document.querySelectorAll('button, .btn-add');
    
    buttons.forEach(btn => {
        btn.addEventListener('mousedown', function() {
            this.style.transform = 'scale(0.95)';
            this.style.boxShadow = '0 0 15px #00ff88';
        });

        btn.addEventListener('mouseup', function() {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = 'none';
        });
    });

    // Auto-hide flash messages after 3 seconds
    const alerts = document.querySelectorAll('.alert');
    if (alerts) {
        setTimeout(() => {
            alerts.forEach(alert => {
                alert.style.opacity = '0';
                alert.style.transition = 'opacity 1s ease';
                setTimeout(() => alert.remove(), 1000);
            });
        }, 3000);
    }
});