import streamlit as st
import numpy as np
import pandas as pd


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Especialización Python for Analytics",
    layout="wide"
)


# ==========================================================
# TÍTULO Y SIDEBAR
# ==========================================================

st.title("Especialización Python for Analytics")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Elena Loayza")

st.image("Python_logo.png", width=300)

st.sidebar.image("DMC.png")


# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

modulos = st.sidebar.selectbox(
    "Seleccione la sección",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)


# ==========================================================
# HOME
# ==========================================================

if modulos == "Home":

    st.header("Proyecto Aplicado en Streamlit")

    st.subheader("Fundamentos de Programación")

    st.write("Nombre: Elena Loayza")
    st.write("Módulo: Python")
    st.write("Año: 2026")

    st.markdown("""
    ### Descripción del proyecto

    Esta aplicación integra los principales conceptos aprendidos
    durante el Módulo 1 de Python mediante una aplicación
    interactiva desarrollada en Streamlit.

    ### Tecnologías utilizadas

    - Python
    - Streamlit
    - NumPy
    - Pandas

    ### Ejercicios desarrollados

    1. Flujo de caja con listas
    2. Registro con NumPy y DataFrame
    3. Uso de funciones
    4. Programación Orientada a Objetos y CRUD
    """)


# ==========================================================
# EJERCICIO 1 - FLUJO DE CAJA CON LISTAS
# ==========================================================

elif modulos == "Ejercicio 1":

    st.header("Ejercicio 1 - Flujo de caja con listas")

    st.markdown("""
    En este ejercicio se registran movimientos financieros
    utilizando una lista. Cada movimiento contiene un concepto,
    un tipo de movimiento y un valor.
    """)

    # Crear lista para guardar los movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input(
        "Ingrese el concepto"
    )

    tipo = st.selectbox(
        "Seleccione el tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Ingrese el valor",
        min_value=0.0,
        step=0.01
    )

    if st.button("Agregar movimiento"):

        if concepto == "":
            st.warning("Ingrese un concepto.")

        elif valor <= 0:
            st.warning("El valor debe ser mayor que cero.")

        else:

            movimiento = [
                concepto,
                tipo,
                valor
            ]

            st.session_state.movimientos.append(
                movimiento
            )

            st.success(
                "Movimiento agregado correctamente."
            )

    # Mostrar movimientos
    if len(st.session_state.movimientos) > 0:

        st.subheader("Movimientos registrados")

        df_movimientos = pd.DataFrame(
            st.session_state.movimientos,
            columns=[
                "Concepto",
                "Tipo",
                "Valor"
            ]
        )

        st.dataframe(
            df_movimientos,
            use_container_width=True
        )

        # Calcular ingresos
        total_ingresos = 0

        # Calcular gastos
        total_gastos = 0

        for movimiento in st.session_state.movimientos:

            if movimiento[1] == "Ingreso":

                total_ingresos = (
                    total_ingresos + movimiento[2]
                )

            elif movimiento[1] == "Gasto":

                total_gastos = (
                    total_gastos + movimiento[2]
                )

        # Calcular saldo
        saldo_final = (
            total_ingresos - total_gastos
        )

        st.subheader("Resumen del flujo de caja")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total de ingresos",
            f"S/ {total_ingresos:.2f}"
        )

        col2.metric(
            "Total de gastos",
            f"S/ {total_gastos:.2f}"
        )

        col3.metric(
            "Saldo final",
            f"S/ {saldo_final:.2f}"
        )

        if saldo_final >= 0:

            st.success(
                "El flujo de caja está a favor."
            )

        else:

            st.error(
                "El flujo de caja está en contra."
            )


# ==========================================================
# EJERCICIO 2 - NUMPY Y DATAFRAME
# ==========================================================

elif modulos == "Ejercicio 2":

    st.header("Ejercicio 2 - NumPy, Arrays y DataFrame")

    st.markdown("""
    En este ejercicio se registran productos mediante arreglos
    de NumPy y posteriormente se muestran en un DataFrame.
    """)

    # Crear arrays
    if "productos" not in st.session_state:
        st.session_state.productos = np.array(
            [],
            dtype=object
        )

    if "categorias" not in st.session_state:
        st.session_state.categorias = np.array(
            [],
            dtype=object
        )

    if "precios" not in st.session_state:
        st.session_state.precios = np.array(
            [],
            dtype=float
        )

    if "cantidades" not in st.session_state:
        st.session_state.cantidades = np.array(
            [],
            dtype=int
        )

    # Formulario
    nombre = st.text_input(
        "Nombre del producto"
    )

    categoria = st.selectbox(
        "Seleccione la categoría",
        [
            "Tecnología",
            "Alimentos",
            "Ropa",
            "Otros"
        ]
    )

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.01
    )

    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    if st.button("Agregar producto"):

        if nombre == "":

            st.warning(
                "Ingrese el nombre del producto."
            )

        elif precio <= 0:

            st.warning(
                "El precio debe ser mayor que cero."
            )

        else:

            st.session_state.productos = np.append(
                st.session_state.productos,
                nombre
            )

            st.session_state.categorias = np.append(
                st.session_state.categorias,
                categoria
            )

            st.session_state.precios = np.append(
                st.session_state.precios,
                precio
            )

            st.session_state.cantidades = np.append(
                st.session_state.cantidades,
                cantidad
            )

            st.success(
                "Producto agregado correctamente."
            )

    # Mostrar DataFrame
    if len(st.session_state.productos) > 0:

        total = (
            st.session_state.precios
            *
            st.session_state.cantidades
        )

        df_productos = pd.DataFrame({

            "Producto":
                st.session_state.productos,

            "Categoría":
                st.session_state.categorias,

            "Precio":
                st.session_state.precios,

            "Cantidad":
                st.session_state.cantidades,

            "Total":
                total
        })

        st.subheader(
            "Registros ingresados"
        )

        st.dataframe(
            df_productos,
            use_container_width=True
        )


# ==========================================================
# EJERCICIO 3 - FUNCIONES
# ==========================================================

elif modulos == "Ejercicio 3":

    st.header("Ejercicio 3 - Funciones")

    st.markdown("""
    En este ejercicio se utilizan funciones relacionadas
    con el área financiera.
    """)

    if "historico" not in st.session_state:
        st.session_state.historico = []

    funcion = st.selectbox(
        "Seleccione una función",
        [
            "Calcular cuota",
            "Calcular interés simple"
        ]
    )

    # ------------------------------------------------------
    # FUNCIÓN PARA CALCULAR CUOTA
    # ------------------------------------------------------

    if funcion == "Calcular cuota":

        capital = st.number_input(
            "Capital",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

        tasa = st.number_input(
            "Tasa por periodo",
            min_value=0.0,
            value=0.05,
            step=0.01
        )

        periodos = st.number_input(
            "Número de periodos",
            min_value=1,
            value=12,
            step=1
        )

        if st.button("Ejecutar función"):

            if tasa == 0:

                cuota = capital / periodos

            else:

                factor = (
                    (1 + tasa)
                    ** periodos
                )

                cuota = capital * (
                    (tasa * factor)
                    /
                    (factor - 1)
                )

            cuota = round(cuota, 2)

            st.success(
                f"La cuota calculada es: S/ {cuota:.2f}"
            )

            st.session_state.historico.append([
                "Calcular cuota",
                capital,
                tasa,
                periodos,
                cuota
            ])

    # ------------------------------------------------------
    # FUNCIÓN PARA CALCULAR INTERÉS
    # ------------------------------------------------------

    else:

        capital = st.number_input(
            "Capital",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

        tasa = st.number_input(
            "Tasa",
            min_value=0.0,
            value=0.05,
            step=0.01
        )

        periodos = st.number_input(
            "Número de periodos",
            min_value=1,
            value=12,
            step=1
        )

        if st.button("Calcular interés"):

            interes = (
                capital
                *
                tasa
                *
                periodos
            )

            interes = round(
                interes,
                2
            )

            st.success(
                f"El interés calculado es: S/ {interes:.2f}"
            )

            st.session_state.historico.append([
                "Calcular interés simple",
                capital,
                tasa,
                periodos,
                interes
            ])

    # Histórico
    if len(st.session_state.historico) > 0:

        st.subheader(
            "Histórico de resultados"
        )

        df_historico = pd.DataFrame(
            st.session_state.historico,
            columns=[
                "Función",
                "Capital",
                "Tasa",
                "Periodos",
                "Resultado"
            ]
        )

        st.dataframe(
            df_historico,
            use_container_width=True
        )


# ==========================================================
# EJERCICIO 4 - POO Y CRUD
# ==========================================================

elif modulos == "Ejercicio 4":

    st.header("Ejercicio 4 - POO y CRUD")

    st.markdown("""
    En este ejercicio se implementan operaciones CRUD:

    Crear
    Leer
    Actualizar
    Eliminar
    """)

    # Clase
    class Producto:

        def __init__(
            self,
            nombre,
            categoria,
            precio
        ):

            self.nombre = nombre
            self.categoria = categoria
            self.precio = precio

        def mostrar(self):

            return {
                "Nombre": self.nombre,
                "Categoría": self.categoria,
                "Precio": self.precio
            }

        def actualizar(
            self,
            nombre,
            categoria,
            precio
        ):

            self.nombre = nombre
            self.categoria = categoria
            self.precio = precio

    # Lista de objetos
    if "productos_crud" not in st.session_state:

        st.session_state.productos_crud = []

    operacion = st.selectbox(
        "Seleccione una operación",
        [
            "Crear",
            "Leer",
            "Actualizar",
            "Eliminar"
        ]
    )

    # ------------------------------------------------------
    # CREAR
    # ------------------------------------------------------

    if operacion == "Crear":

        st.subheader(
            "Crear registro"
        )

        nombre = st.text_input(
            "Nombre del producto"
        )

        categoria = st.text_input(
            "Categoría"
        )

        precio = st.number_input(
            "Precio",
            min_value=0.0,
            step=0.01
        )

        if st.button(
            "Crear registro"
        ):

            if nombre == "":

                st.warning(
                    "Ingrese el nombre."
                )

            elif categoria == "":

                st.warning(
                    "Ingrese la categoría."
                )

            elif precio <= 0:

                st.warning(
                    "El precio debe ser mayor que cero."
                )

            else:

                producto = Producto(
                    nombre,
                    categoria,
                    precio
                )

                st.session_state.productos_crud.append(
                    producto
                )

                st.success(
                    "Registro creado correctamente."
                )

    # ------------------------------------------------------
    # LEER
    # ------------------------------------------------------

    elif operacion == "Leer":

        st.subheader(
            "Registros"
        )

        if len(
            st.session_state.productos_crud
        ) == 0:

            st.info(
                "No existen registros."
            )

        else:

            registros = []

            for producto in (
                st.session_state.productos_crud
            ):

                registros.append(
                    producto.mostrar()
                )

            df_crud = pd.DataFrame(
                registros
            )

            st.dataframe(
                df_crud,
                use_container_width=True
            )

    # ------------------------------------------------------
    # ACTUALIZAR
    # ------------------------------------------------------

    elif operacion == "Actualizar":

        st.subheader(
            "Actualizar registro"
        )

        if len(
            st.session_state.productos_crud
        ) == 0:

            st.info(
                "No existen registros para actualizar."
            )

        else:

            numero = st.number_input(
                "Número del registro",
                min_value=1,
                max_value=len(
                    st.session_state.productos_crud
                ),
                step=1
            )

            producto = (
                st.session_state.productos_crud[
                    numero - 1
                ]
            )

            nuevo_nombre = st.text_input(
                "Nuevo nombre",
                value=producto.nombre
            )

            nueva_categoria = st.text_input(
                "Nueva categoría",
                value=producto.categoria
            )

            nuevo_precio = st.number_input(
                "Nuevo precio",
                min_value=0.0,
                value=float(
                    producto.precio
                ),
                step=0.01
            )

            if st.button(
                "Actualizar registro"
            ):

                producto.actualizar(
                    nuevo_nombre,
                    nueva_categoria,
                    nuevo_precio
                )

                st.success(
                    "Registro actualizado correctamente."
                )

    # ------------------------------------------------------
    # ELIMINAR
    # ------------------------------------------------------

    else:

        st.subheader(
            "Eliminar registro"
        )

        if len(
            st.session_state.productos_crud
        ) == 0:

            st.info(
                "No existen registros para eliminar."
            )

        else:

            numero = st.number_input(
                "Número del registro a eliminar",
                min_value=1,
                max_value=len(
                    st.session_state.productos_crud
                ),
                step=1
            )

            if st.button(
                "Eliminar registro"
            ):

                st.session_state.productos_crud.pop(
                    numero - 1
                )

                st.success(
                    "Registro eliminado correctamente."
                )
