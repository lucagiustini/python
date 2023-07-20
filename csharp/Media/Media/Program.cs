using System;
using System.Xml.Linq;

int numero_elementi;
int max;
int min;
float media;
int temp;

do
{
    Console.WriteLine("Quanti elementi abbiamo? Inserisci il numero di elementi: ");
    numero_elementi = Convert.ToInt32(Console.ReadLine());
} while (numero_elementi < 2);

int[] vettore = new int[numero_elementi];

for (int i = 0; i < numero_elementi; i++)
{
    Console.WriteLine("Inserisci gli elementi: ");
    vettore[i] = Convert.ToInt32(Console.ReadLine());
}

for (int i = 0; i < numero_elementi; i++)
{
    for (int j = 0; j < numero_elementi - i - 1; j++)
    {
        if (vettore[j] < vettore[j + 1])
        {
            // in ordine decrescente
            temp = vettore[j];
            vettore[j] = vettore[j + 1];
            vettore[j + 1] = temp;
        }
    }

}

media = vettore[0];

for (int i = 1; i < numero_elementi; i++)
{
    media = media + vettore[i];
}

max = vettore[0];
min = vettore[numero_elementi - 1];
media = media / numero_elementi;

Console.WriteLine();
Console.WriteLine("Il massimo dei numeri del vettore è : " + max);
Console.WriteLine();
Console.WriteLine("Il minimo dei numeri del vettore è : " + min);
Console.WriteLine();
Console.WriteLine("La media dei numeri del vettore è : " + media);
Console.WriteLine();

Console.WriteLine("Vettore: ");
Console.WriteLine($"{string.Join(", ", vettore)}");