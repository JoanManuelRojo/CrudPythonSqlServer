import InterfazGrafica
import tkinter
import sqlServerCon


def main():
    root = InterfazGrafica.Tk()
    root.wm_title("Crud Python SQL Server")
    #app = InterfazGrafica(root)
    #app.mainloop()

    print(sqlServerCon.queryConsulta())

# if __name__ == "__main__":

#   main()