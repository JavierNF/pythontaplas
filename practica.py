
import pandas as pd
import matplotlib.pyplot as plt



def cargar_archivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Campus\\programacion\\Programacion\\proyectos\\excel2\\Servei_d_aigua_-usos_i_nombre_de_clients-.csv")
    # datos = datos[["Ús","any_","m3_registrats","núm_clients","ObjectId","CODI_ENS","NOM_ENS"]]
    df = datos[["m3_registrats", "núm_clients"]]

    df = datos.rename(columns={
        "m3_registrats": "m3",
        "núm_clients": "clientes",

    })

    #print(df.sample(5))


    #grafico de barras
    valor_por_ciudad = df.groupby("m3")["clientes"].mean()
    valor_por_ciudad.head(10).plot.barh()
    plt.show()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     #print_hi('PyCharm')
     cargar_archivo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/