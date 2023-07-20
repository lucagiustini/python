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
            int marco;
            int gigi;

            marco = Convert.ToInt32(Console.ReadLine());
            gigi= Convert.ToInt32(Console.ReadLine());

            if (marco > 10 && gigi > 10) // AND
            {
                Console.WriteLine("AND sburo alla festa");
            }
            if (marco > 10 || gigi > 10) // OR
            {
                Console.WriteLine("OR sburo alla festa");
            }
            if (marco != 10) // NOT
            {
                Console.WriteLine("NOT sburo alla festa");
            }
            if (marco > 10 ^ gigi > 10) // XOR
            {
                Console.WriteLine("XOR sburo alla festa");
            }
        }
    }
}