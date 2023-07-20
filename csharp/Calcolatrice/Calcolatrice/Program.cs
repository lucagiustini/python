using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pino
{
    class Programmino
    {
        static void Main()
        {
            int scelta;
            int n1;
            int n2;
            int risultato;
            string continua;

            do
            {
                Console.WriteLine("Quale operazione vuoi eseguire? /n Sceglina una da vero bomber:");
                Console.WriteLine();
                Console.WriteLine("1 - somma");
                Console.WriteLine("2 - sottrazione");
                Console.WriteLine("3 - moltiplicazione");
                Console.WriteLine("4 - divisione");
                Console.WriteLine("9 - exit");
                scelta = Convert.ToInt32(Console.ReadLine());

                if (scelta != 9)
                {
                    switch (scelta)
                    {
                        case 1:
                            Console.Write("scrivi il primo addendo: ");
                            n1 = Convert.ToInt32(Console.ReadLine());
                            Console.Write("scrivi il secondo addendo: ");
                            n2 = Convert.ToInt32(Console.ReadLine());
                            risultato = n1 + n2;
                            Console.WriteLine("il risultato: " + risultato);
                            break;
                        case 2:
                            Console.Write("scrivi il primo addendo: ");
                            n1 = Convert.ToInt32(Console.ReadLine());
                            Console.Write("scrivi il secondo addendo: ");
                            n2 = Convert.ToInt32(Console.ReadLine());
                            risultato = n1 - n2;
                            Console.WriteLine("il risultato: " + risultato);
                            break;
                        case 3:
                            Console.Write("scrivi il primo addendo: ");
                            n1 = Convert.ToInt32(Console.ReadLine());
                            Console.Write("scrivi il secondo addendo: ");
                            n2 = Convert.ToInt32(Console.ReadLine());
                            risultato = n1 * n2;
                            Console.WriteLine("il risultato: " + risultato);
                            break;
                        case 4:
                            Console.Write("scrivi il primo addendo: ");
                            n1 = Convert.ToInt32(Console.ReadLine());
                            Console.Write("scrivi il secondo addendo: ");
                            n2 = Convert.ToInt32(Console.ReadLine());
                            risultato = n1 / n2;
                            Console.WriteLine("il risultato: " + risultato);
                            break;
                        //case 9:
                            //Console.Write("Ciao!"); break;
                    }
                }
                else
                {
                    Console.Write("Ciao!");
                    return;
                }

                Console.Write(" per continuare scrivi: si ");
                continua = Console.ReadLine();

            } while (continua == "si") ;
        }
    }
}