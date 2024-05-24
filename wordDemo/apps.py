from django.apps import AppConfig

# "wordDemo" Django uygulaması için özel bir AppConfig sınıfı tanımla
class WorddemoConfig(AppConfig):
    # Model anahtarları için BigAutoField kullanılması için default_auto_field özniteliğini ayarla
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Django uygulamasının adını belirle, bu da 'wordDemo'
    name = 'wordDemo'
