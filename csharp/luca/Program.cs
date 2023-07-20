using System;

//struct data
//{
//    public int giorno;
//    public int mese;
//    public int anno;
//};

//struct orario
//{
//    public int ore;
//    public int minuti;
//};

//struct corpo_celeste
//{
//    public char codice[50];
//    public int tipologia; //0-pianeta, 1-satellite
//    public char nome[100]; //non contiene spazi
//};

//struct evento
//{
//    public char codice[50];
//    public struct corpo_celeste *ptrCorpo; //puntatore al corpo celeste
//    public struct data data_evento; // data dell'evento
//    pub0lic struct orario; //orario di inizio dell'evento
//    public char nome[100]; //non contiene spazi
//    public int durata; //in minuti
//};

//public const int NMAX_CORPI = 100;
//public const int NMAX_EVENTI = 200;

//public int nrCorpiCelest;
//public int nrEventiAstronomici;


//struct corpo_celeste corpi[NMAX_CORPI];
//struct evento eventi_astronomici[NMAX_EVENTI];


//struct corpo_celeste *cercaCorpo(char id_corpo[], struct corpo_celeste el_corpi[])


//static class Program_1
//{
//    static void Main()
//    {
//        var d = 12;
//        //var d = 12;
//        var t = 4;
//        string parola;
//        int variabile;

//        d = 16;

//        var s = d / t;
//        Console.WriteLine("Apparently 12 / 4 is...");
//        parola = Console.ReadLine();
//        Console.WriteLine("hai inserito la parola: " + parola);
//        variabile = Convert.ToInt32(Console.ReadLine());
//        Console.WriteLine("hai inserito il numero: " + variabile);
//        Console.ReadKey();
//    }
//}

static class Program
{
    static void Main()
    {
        int numero;
        int j = 0;
        int k = 0;

        Console.WriteLine();
        Console.WriteLine("inserisci il numero: ");
        numero = Convert.ToInt32( Console.ReadLine() );
        Console.WriteLine("i numeri che vanno da 0 a " + numero + "sono: ");
        Console.WriteLine();
        Console.WriteLine("ciclo FOR: ");
        for (int i = 0;i < numero+1; i++)
        {
            Console.WriteLine(i);
        }

        Console.WriteLine("inserisci il numero: ");
        numero = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine();
        Console.WriteLine("ciclo WHILE: ");
        while (j < numero+1)
        {
            j ++;
            Console.WriteLine(j-1);
        }

        Console.WriteLine();
        Console.WriteLine("inserisci il numero: ");
        numero = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("ciclo DO: ");
        do
        {
            k = k + 1;
            Console.WriteLine(k-1);
        } while (k < numero+1);
    }
}