from django.db import models

class RealState(models.Model):
    id = models.AutoField(primary_key=True)
    SalePrice = models.CharField(max_length=255)
    YearBuilt = models.FloatField()
    YrSold = models.FloatField()
    MonthSold = models.FloatField()
    Size_sqf = models.FloatField()
    Floor = models.FloatField()
    HallwayType = models.CharField(max_length=50)
    HeatingType = models.CharField(max_length=50)
    AptManageType = models.CharField(max_length=50)
    TimeToBusStop = models.CharField(max_length=20)
    TimeToSubway = models.CharField(max_length=20)
    N_APT = models.FloatField()
    N_manager = models.FloatField()
    SubwayStation = models.CharField(max_length=50)
    N_FacilitiesNearBy_PublicOffice = models.FloatField()
    N_FacilitiesNearBy_Hospital = models.FloatField()
    N_FacilitiesNearBy_Departmentstore = models.FloatField()
    N_FacilitiesNearBy_Mall = models.FloatField()
    N_FacilitiesNearBy_ETC = models.FloatField()
    N_FacilitiesNearBy_Park = models.FloatField()
    N_SchoolNearBy_Elementary = models.FloatField()
    N_SchoolNearBy_Middle = models.FloatField()
    N_SchoolNearBy_High = models.FloatField()
    N_SchoolNearBy_University = models.FloatField()
    N_FacilitiesInApt = models.FloatField()
    N_FacilitiesNearBy_Total = models.FloatField()
    N_SchoolNearBy_Total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'realState'

class DimTiempo(models.Model):
    id = models.AutoField(primary_key=True)
    YearBuilt = models.FloatField()
    YrSold = models.FloatField()
    MonthSold = models.FloatField()

    class Meta:
        managed = False
        db_table = 'DimTiempo'

class DimUbicacion(models.Model):
    id = models.AutoField(primary_key=True)
    TimeToBusStop = models.CharField(max_length=20)
    TimeToSubway = models.CharField(max_length=20)
    SubwayStation = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'DimUbicacion'

class DimTamaño(models.Model):
    id = models.AutoField(primary_key=True)
    Size_sqf = models.FloatField()
    Floor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'DimTamaño'

class DimFacilidades(models.Model):
    id = models.AutoField(primary_key=True)
    N_FacilitiesNearBy_PublicOffice = models.FloatField()
    N_FacilitiesNearBy_Hospital = models.FloatField()
    N_FacilitiesNearBy_Departmentstore = models.FloatField()
    N_FacilitiesNearBy_Mall = models.FloatField()
    N_FacilitiesNearBy_ETC = models.FloatField()
    N_FacilitiesNearBy_Park = models.FloatField()
    N_SchoolNearBy_Elementary = models.FloatField()
    N_SchoolNearBy_Middle = models.FloatField()
    N_SchoolNearBy_High = models.FloatField()
    N_SchoolNearBy_University = models.FloatField()
    N_FacilitiesInApt = models.FloatField()
    N_FacilitiesNearBy_Total = models.FloatField()
    N_SchoolNearBy_Total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'DimFacilidades'

class DimVenta(models.Model):
    id = models.AutoField(primary_key=True)
    SalePrice = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'DimVenta'

class HechosVentas(models.Model):
    id = models.AutoField(primary_key=True)
    VentaId = models.ForeignKey(DimVenta, on_delete=models.CASCADE)
    TiempoId = models.ForeignKey(DimTiempo, on_delete=models.CASCADE)
    UbicacionId = models.ForeignKey(DimUbicacion, on_delete=models.CASCADE)
    TamañoId = models.ForeignKey(DimTamaño, on_delete=models.CASCADE)
    FacilidadesId = models.ForeignKey(DimFacilidades, on_delete=models.CASCADE)
    VentaPromedio = models.FloatField()
    NumPropiedadesVendidas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'HechosVentas'


    class Meta:
        managed = False
        db_table = 'HechosVentas'