using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Libro
{
    int pag_iniziale;
    int pag_corrente;
    int pag_finale;

    public Libro(int pagina_i, int pagina_c, int pagina_f)
    {
        pag_iniziale = pagina_i;
        pag_corrente= pagina_c;
        pag_finale = pagina_f;
    }
    public void Sfoglia_Avanti()
    {
        if (pag_corrente == pag_finale)
        {
            Console.WriteLine(" sei già all'ultima pagina !!! ");
        }
        else
        {
            pag_corrente++;
            Console.WriteLine(" sei alla pagina " + pag_corrente);
        }
    }

    public void Sofglia_Indietro()
    {
        if (pag_corrente == pag_iniziale)
        {
            Console.WriteLine(" sei alla pagina iniziale !!! ");
        }
        else
        {
            pag_corrente--;
            Console.WriteLine(" sei alla pagina " + pag_corrente);
        }

    }
}