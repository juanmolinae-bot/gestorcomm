from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.incidencias.models import Zona, Incidencia


class Command(BaseCommand):
    help = 'Carga datos demo: usuario juan y 4 incidencias de ejemplo'

    def handle(self, *args, **options):
        # Crear superusuario si no existe
        if not User.objects.filter(username='juan').exists():
            u = User.objects.create_superuser('juan', 'juan@demo.cl', 'demo1234')
            self.stdout.write(self.style.SUCCESS('Usuario juan creado'))
        else:
            u = User.objects.get(username='juan')
            self.stdout.write('Usuario juan ya existe')

        # Crear zonas
        z1, _ = Zona.objects.get_or_create(nombre='Inversores', defaults={'descripcion': 'Sector inversores ASIII'})
        z2, _ = Zona.objects.get_or_create(nombre='BESS Cristales', defaults={'descripcion': 'Sistema de almacenamiento'})
        z3, _ = Zona.objects.get_or_create(nombre='SE Futuro', defaults={'descripcion': 'Subestacion 220/33 kV'})

        # Crear incidencias solo si no hay ninguna
        if Incidencia.objects.count() == 0:
            Incidencia.objects.create(
                titulo='Falla comunicacion inversor INV-12',
                descripcion='No responde a polling modbus desde SCADA. Revisar fibra y switch.',
                zona=z1, prioridad='alta', estado='abierta', responsable=u
            )
            Incidencia.objects.create(
                titulo='Alarma BMS celda 3 rack 7',
                descripcion='Voltaje fuera de rango. Revisar conexion CAN.',
                zona=z2, prioridad='critica', estado='en_revision', responsable=u
            )
            Incidencia.objects.create(
                titulo='OLTC transformador T1 no opera',
                descripcion='Tap changer no responde a comando remoto desde sala de control.',
                zona=z3, prioridad='alta', estado='en_revision', responsable=u
            )
            Incidencia.objects.create(
                titulo='Tracker fila 24 desalineado',
                descripcion='Tracker no sigue posicion comandada, revisar GCU.',
                zona=z1, prioridad='media', estado='resuelta', responsable=u
            )
            self.stdout.write(self.style.SUCCESS('4 incidencias demo creadas'))
        else:
            self.stdout.write('Ya existen incidencias, no se crean duplicados')

        self.stdout.write(self.style.SUCCESS('Seed completado.'))
