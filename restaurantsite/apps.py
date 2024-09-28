from django.apps import AppConfig


class RestaurantsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurantsite'

    def ready(self):
        import restaurantsite.signals