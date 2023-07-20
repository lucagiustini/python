using System;
using System.Text;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace OrdinamLog
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 5;
            int[] vettore = new int[5];
            vettore[0] = 98;
            vettore[1] = 55;
            vettore[2] = 6;
            vettore[3] = 17;
            vettore[4] = 4;

            Bubblesord(vettore, n);

            for(int i = 0; i < n; i++)
            {
                Console.WriteLine( vettore[i]);
            }
        }

        static void Bubblesord(int[] vet, int n)
        {
            int temp; // valore scambio
            int top = 0;
            bool scambio;
            int ultimoscambio = 0;
            int i;

            do { 
                scambio = false;
                for(i = n - 1; i > top; i--)
                {
                    if (vet[i] < vet[i - 1])
                    {
                        temp = vet[i];
                        vet[i] = vet[i - 1];
                        vet[i - 1] = temp;

                        scambio = true;
                        ultimoscambio = i;
                    }
                }
                top = ultimoscambio;
            } while (scambio);

            // top = 0, ultimoscambio = 0
            // scambio = false | i = 4 | 98, 55, 6, 17, 4 -> 98, 55, 6, 4, 17 | ultimoscambio = 4 | top = 0 | scambio = true
            // scambio = true | i = 3 | 98, 55, 6, 4, 17 -> 98, 55, 4, 6, 17 | ultimoscambio = 3 | top = 0 | scambio = true
            // scambio = true | i = 2 | 98, 55, 4, 6, 17 -> 98, 4, 55, 6, 17 | ultimoscambio = 2 | top = 0 | scambio = true
            // scambio = true | i = 1 | 98, 55, 4, 6, 17 -> 4, 98, 55, 6, 17 | ultimoscambio = 1 | top = 0 | scambio = true
            // scambio = true | i = 0 | ************************************ | ultimoscambio = 1 | top = 1 | scambio = true

            // top = 1, ultimoscambio = 1
            // scambio = false | i = 4 | 4, 98, 55, 6, 17 -> 4, 98, 55, 6, 17 | ultimoscambio = 4 | top = 1 | scambio = true
            // scambio = true | i = 3 | 4, 98, 55, 6, 17 -> 4, 98, 6, 55, 17 | ultimoscambio = 3 | top = 1 | scambio = true
            // scambio = true | i = 2 | 4, 98, 6, 55, 17 -> 4, 6, 98, 55, 17 | ultimoscambio = 2 | top = 1 | scambio = true
            // scambio = true | i = 1 | ************************************ | ultimoscambio = 2 | top = 2 | scambio = true

            // top = 2, ultimoscambio = 2
            // scambio = false | i = 4 | 4, 6, 98, 55, 17 -> 4, 6, 98, 17, 55 | ultimoscambio = 4 | top = 2 | scambio = true
            // scambio = true | i = 3 | 4, 6, 98, 17, 55 -> 4, 6, 17, 98, 55 | ultimoscambio = 3 | top = 2 | scambio = true
            // scambio = true | i = 2 | ************************************ | ultimoscambio = 3 | top = 3 | scambio = true

            // top = 3, ultimoscambio = 3
            // scambio = false | i = 4 | 4, 6, 17, 98, 55 -> 4, 6, 17, 55, 98 | ultimoscambio = 4 | top = 3 | scambio = true
            // scambio = true | i = 3 | ************************************ | ultimoscambio = 4 | top = 4 | scambio = true

            // top = 4, ultimoscambio = 4
            // scambio = false | i = 4 | ************************************ | ultimoscambio = 4 | top = 4 | scambio = false

            // END
        }
    }
}