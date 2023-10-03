using System;

namespace CalculadoraConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Calculadora de Soma");
            Console.WriteLine("------------------");

            Console.Write("Digite o primeiro número: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            double num2 = Convert.ToDouble(Console.ReadLine());

            double resultado = num1 + num2;

            Console.WriteLine($"O resultado da soma é: {resultado}");

            Console.WriteLine("Pressione qualquer tecla para sair.");
            Console.ReadKey();
        }
    }
}
