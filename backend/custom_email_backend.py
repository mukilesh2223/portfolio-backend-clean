import ssl
from django.core.mail.backends.smtp import EmailBackend

class NoSSLEmailBackend(EmailBackend):
    def open(self):
        # Disable SSL Certificate Validation (Fix for Windows/Python bug)
        self.ssl_context = ssl._create_unverified_context()
        return super().open()
