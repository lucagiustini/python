using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ordinamento
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numeri = new int[5] { 10, 8, 9, 54, 32 };
            Console.WriteLine();
            OrdinaVet(numeri);
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(numeri[i]);
            }
            Console.ReadKey();
        }

        static void OrdinaVet(int[] vet)
        {
            int temp;
            for (int i = 0; i < vet.Length - 1; i++)
            {
                for(int j = i + 1; j < vet.Length; j++)
                {
                    if (vet[j] > vet[i])
                    {
                        temp = vet[j];
                        vet[j] = vet[i];
                        vet[i] = temp;
                    }
                }
            }

            /*            for (int i = 0; i < vet.Length; i++)
                            {
                                for(int j = i; j < vet.Length; j++)
                                {
                                }
                            }
             */

            // 10, 8, 9, 54, 32 ** i = 0 ** j = 0 INUTILE QUINDI LINE 28 (int j = i + 1;

            // 10, 8, 9, 54, 32 ** i = 0 ** j = 1
            // 9, 8, 10, 54, 32 ** i = 0 ** j = 2
            // 54, 8, 10, 9, 32 ** i = 0 ** j = 3
            // 54, 8, 10, 9, 32 ** i = 0 ** j = 4

            // 54, 8, 10, 9, 32 ** i = 1 ** j = 1 INUTILE QUINDI LINE 28 (int j = i + 1;

            // 54, 10, 8, 9, 32 ** i = 1 ** j = 2
            // 54, 10, 8, 9, 32 ** i = 1 ** j = 3
            // 54, 32, 8, 9, 10 ** i = 1 ** j = 4

            // 54, 32, 8, 9, 10 ** i = 2 ** j = 2 INUTILE QUINDI LINE 28 (int j = i + 1;

            // 54, 32, 9, 8, 10 ** i = 2 ** j = 3
            // 54, 32, 10, 8, 9 ** i = 2 ** j = 4

            // 54, 32, 10, 8, 9 ** i = 3 ** j = 3 INUTILE QUINDI LINE 28 (int j = i + 1;

            // 54, 32, 10, 9, 8 ** i = 3 ** j = 4

            // 54, 32, 10, 9, 8 ** i = 4 ** j = 4   INUTILE, QUINDI
            // NELLA LINE 26 for (int i = 0; i < vet.Length - 1; i++)
            // ABBIAMO IL ;i < vet.Length - 1;

        }
    }
}