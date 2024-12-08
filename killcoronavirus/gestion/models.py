from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, choices=[('Médico', 'Médico'), ('Administrador', 'Administrador')])

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.tipo_usuario}"


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_especialidad


class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    numero_colegio_medico = models.CharField(max_length=20)
    especialidades = models.ManyToManyField(Especialidad, through='MedicoEspecialidad')

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido}"


class MedicoEspecialidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)


class Paciente(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"


class FichaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    anamnesis = models.TextField()
    diagnostico = models.TextField()

    def __str__(self):
        return f"Ficha {self.id} - {self.paciente}"


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class RecetaMedica(models.Model):
    ficha = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    indicaciones = models.TextField()

    def __str__(self):
        return f"Receta {self.id} - {self.ficha.paciente}"


class Examen(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class ExamenesSolicitados(models.Model):
    ficha = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)

    def __str__(self):
        return f"Examen solicitado: {self.examen.nombre} - {self.ficha.paciente}"