# Blog api rest #

Aplicacion Web hecha con python y Django como Framework, se recomienda crear un entorno virtual donde se instalaran las librerias requeridas.

### Poner en marcha ###

* Clonar repositorio
    
    ```Aqui va la url para clonarlo```

* Instalar librerias de acuerdo a la version en requirements.txt
    
    ```$ pip install -r requirements.txt```

    Ojo: puede que sea necesario actualizar pip

    ```$ pip install --upgrade pip setuptools```

* Instalar librerias de acuerdo a la version en requirements_dev.txt solo para desarrollo
    
    ```$ pip install -r requirements_dev.txt```

* Aplicar migrate

    ```$ ./manage.py migrate```
* Para desarrollo se utilizo un entorno Codan(Opcional)
    ```$ conda create -n py36 python=3.6```
<!-- * Cargar datos iniciales, para esto se debe crear primero el superusuario
    
    ```
    $ ./manage.py loaddata FIXTURE/catalogos.json
    ```


    ```
    $ ./manage.py loaddata FIXTURE/productos.json
    ``` -->

<!-- 
* cargar permisos para usuarios en el admin

    ``` from sacp import permissions ```
    ``` permissions.addpermission() ``` -->

### local settings ###

<!-- * Router en bases de datos, para el manejo del router, en el local_settings.py se agregan las bases de datos a utilizar, teniendo en cuenta que se debe tener una default ya establecida, en las siguientes lineas se puede ver un ejemplo:
    ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'sacp',
                'USER': 'admin',
                'PASSWORD': 'devtest',
                'HOST': '192.168.1.191',
                'PORT': '8432',  
            },
            'xcumpich_db': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'sacp',
                'USER': 'admin',
                'PASSWORD': 'devtest',
                'HOST': '192.168.1.191',
                'PORT': '8432',    
            },
            'tamanche_db': {    
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'sacp',
                'USER': 'admin',
                'PASSWORD': 'devtest',
                'HOST': '192.168.1.196',
                'PORT': '8432',    
            }
        }
    ```

* Se agregan las siguientes variables ya definidas
    ```
        DATABASE_ROUTERS = ['sacp.router.MyRouter',]

        DB_Mapping = {
            "xcumpich": "xcumpich_db",
            "tamanche": "tamanche_db",
        }
    ``` -->

