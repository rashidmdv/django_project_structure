from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# from apps.accounts.models import Role
from ...models.user import Role


class Command(BaseCommand):
    help = "Seed initial admin role and admin user"

    def handle(self, *args, **options):
        User = get_user_model()

        #  Create Admin Role
        admin_role, role_created = Role.objects.get_or_create(
            name="admin",
            defaults={"is_active": True}
        )

        if role_created:
            self.stdout.write(self.style.SUCCESS("Admin role created"))
        else:
            self.stdout.write("Admin role already exists")

        # Create Admin User
        email = "admin@gmail.com"
        password = "123456"

        if not User.objects.filter(email=email).exists():
            admin_user = User.objects.create_user(
                email=email,
                password=password,
                username="admin",
                role=admin_role,
                is_staff=True,
                is_active=True,
            )
            self.stdout.write(self.style.SUCCESS("Admin user created"))
        else:
            self.stdout.write("Admin user already exists")

        self.stdout.write(self.style.SUCCESS("Seeding completed"))
