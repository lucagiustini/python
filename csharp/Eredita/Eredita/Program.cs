using System;
using System.Security.Cryptography.X509Certificates;

namespace luca2
{
    class Program
    {
        static void Main(string[] args)
        {
            Padre x = new Padre();
            Figlio y = new Figlio();
            //x.Equals(y);
            x.Presentazione(50);
            y.Confronto(20);
        }
    }

    class Padre
    {
        protected int anni = 50;
        public void Presentazione(int i)
        {
            anni = i;
            Console.WriteLine(" Ciao sono il padre e ho "+ anni + " anni");
        }
        
    }

    class Figlio : Padre
    {
        public void Confronto(int differenza)
        {
            anni = anni - differenza;
            Console.WriteLine(" Ciao sono il figlio. Ho " + differenza + " di differenza con mio padre. ");
            Console.Write(" Quindi ho " + anni + " anni !!!");
        }
    }
}