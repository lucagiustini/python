using System;

namespace luca
{
    class Program
    {
        static void Main(string[] args)
        {
            Libro horror = new Libro(1, 3, 3);
            horror.Sfoglia_Avanti();

            Libro ciccioletto = new Libro(1, 3, 3);
            ciccioletto.Sofglia_Indietro();

            Libro daje= new Libro(1, 3, 3);
            daje.Sofglia_Indietro();
            daje.Sofglia_Indietro();
            daje.Sofglia_Indietro();
        }
    }
}