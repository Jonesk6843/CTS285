using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// CTS 285
// M1T1
// Kent Jones
// 8/23/23
namespace M1T1_Orientation_Jones
{
    internal class M1T1_Jones
    {
        static void Main(string[] args)
        {
            // Inputting lambda expression
            Action<string> Display = str => Console.WriteLine(str);

            //Typing out general information, interests, and other info about myself
            Display("Hello! My name is Kent Jones Jr!");
            Console.WriteLine();
            Display("Currently. I am learning C++ with professor Norris.");
            Console.WriteLine();
            Display("Some of my hobbies include writing stories, going on jogs, and playing video games.");
            Console.WriteLine();
            Display("During my college journey, I have learned C#, C++, JavaScript, HTML, Python, SQL, and Oracle Databasing." + "\n" + 
                "Out of all of these languages, I enjoy programming in Java and C# the most.");
            Console.WriteLine();
            Display("As for my partner for the first HW assignment, I did not catch their name.");

            //Getting user input
            Console.Write("*Press enter to end this interaction*");
            string exitInput = Console.ReadLine();
        }
    }
}
