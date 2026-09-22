import streamlit as st
import numpy as np
import pandas as pd


# ==========================================================
# DISEÑO CON HTML, CSS Y JAVASCRIPT
# ==========================================================

st.markdown("""
<style>

/* Fondo general */
.stApp {
    background: linear-gradient(135deg, #f5f7fa, #e8edf3);
}

/* Título principal */
h1 {
    color: #1F4E79;
    text-align: center;
    font-weight: 700;
    animation: aparecer 0.8s ease-in-out;
}

/* Subtítulos */
h2, h3 {
    color: #1F4E79;
}

/* Botones */
.stButton > button {
    background-color: #1F4E79 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px;
    padding: 8px 20px;
    transition: all 0.3s ease;
}

/* Animación e iluminación al interactuar */
.stButton > button:hover {
    background-color: #163A5C !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    transform: scale(1.03);
    box-shadow: 0 0 18px rgba(31, 78, 121, 0.6);
}

/* Campos de texto */
.stTextInput input,
.stNumberInput input {
    border-radius: 7px;
    border: 1px solid #B8C5D1;
    transition: all 0.3s ease;
}

/* Iluminación al interactuar */
.stTextInput input:focus,
.stNumberInput input:focus {
    border-color: #1F4E79;
    box-shadow: 0 0 12px rgba(31, 78, 121, 0.30);
}

/* Selectbox */
div[data-baseweb="select"] {
    border-radius: 7px;
    transition: all 0.3s ease;
}

div[data-baseweb="select"]:hover {
    box-shadow: 0 0 12px rgba(31, 78, 121, 0.20);
}

/* Métricas */
[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 18px rgba(31, 78, 121, 0.25);
}

/* Tablas */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
}

/* Animación de entrada */
@keyframes aparecer {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animacion {
    animation: aparecer 0.8s ease-in-out;
}

</style>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const app = document.querySelector(".stApp");
    if (app) {
        app.classList.add("animacion");
    }
});
</script>
""", unsafe_allow_html=True)



# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.title("Especialización Python for Analytics")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Elena Loayza")


st.image("Python_logo.png", width=300)

st.sidebar.image("DMC.png")


# ==========================================================
# MENÚ
# ==========================================================

modulos = st.sidebar.selectbox(
    "Seleccione el módulo",
    [
        "Listas",
        "Arreglos",
        "Funciones",
        "POO"
    ]
)


# ==========================================================
# LISTAS
# ==========================================================

if modulos == "Listas":

    st.write("Te encuentras en el módulo de listas")

    st.subheader("Flujo de caja con listas")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input(
        "Ingrese el concepto"
    )

    tipo = st.selectbox(
        "Seleccione el tipo de movimiento",
        [
            "Ingreso",
            "Gasto"
        ]
    )

    valor = st.number_input(
        "Ingrese el valor",
        min_value=0.0,
        step=0.01
    )

    if st.button("Agregar movimiento"):

        if concepto == "":
            st.warning(
                "Ingrese un concepto."
            )

        elif valor <= 0:
            st.warning(
                "El valor debe ser mayor que cero."
            )

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


    # Mostrar lista de movimientos

    if len(st.session_state.movimientos) > 0:

        st.subheader(
            "Movimientos registrados"
        )

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

        for movimiento in st.session_state.movimientos:

            if movimiento[1] == "Ingreso":

                total_ingresos = (
                    total_ingresos + movimiento[2]
                )


        # Calcular gastos

        total_gastos = 0

        for movimiento in st.session_state.movimientos:

            if movimiento[1] == "Gasto":

                total_gastos = (
                    total_gastos + movimiento[2]
                )


        # Calcular saldo

        saldo_final = (
            total_ingresos - total_gastos
        )


        st.subheader(
            "Resumen"
        )

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
# ARREGLOS
# ==========================================================

elif modulos == "Arreglos":

    st.write("Te encuentras en el módulo de arreglos")

    st.subheader(
        "Registro con NumPy y DataFrame"
    )

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


    cantidad = st.slider(
        "Seleccione la cantidad",
        min_value=1,
        max_value=100,
        value=20
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
# FUNCIONES
# ==========================================================

elif modulos == "Funciones":

    st.write(
        "Te encuentras en el módulo de Funciones"
    )

    st.subheader(
        "Funciones financieras"
    )


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
    # CALCULAR CUOTA
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


            cuota = round(
                cuota,
                2
            )


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
    # CALCULAR INTERÉS
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
# POO
# ==========================================================

else:

    st.write(
        "Te encuentras en el módulo de POO"
    )

    st.subheader(
        "Programación Orientada a Objetos"
    )


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


    # Lista de productos

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
