using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Something
{
    class cheatsheet {
        static void Main (string[] args)
        {
            //SYNTAX AND GENERAL KNOWLEDGE

            int mathexample = Math.Abs(-7-39274);
            CheatObjectsandClass sweet = new CheatObjectsandClass("swag"); // object -- like java
            sweet.field1 = "sexy";

            /*
            ---Methods---
                *return statemen

            */

            // VARIABLES
            /* Data Types
            
            to convert string to int, 
            ---Strings---

            --Numbers--
            
            */
            int a = 0;
            double c = 2.9;
            string b = "45";
            bool truth = true;
            int str2num = Convert.ToInt32(b); // converts string to number  
            
            //STATEMENTS
            /*
            */
            //print statement
            Console.WriteLine("Hello World"); // typical print rules apply
            //pause program
            Console.ReadLine(); //allow window to stay and pauses program and reads user input
            //user input
            Console.Write("The greeting message goes here: ");


            //DATA STRUCTURES

            /**/
            //---Arrays---
            // initialize
            int[] arr = {1,2,3};
            int[] empty = new int[10]; // same as java
            // 2d array
            int[,] numberGrid = {
                {1,2 },
                {3,4 },
                {5,6 }
            }
            int[,] = new int[10,10]; //same needs as java

            //LOOPS
                
                //---FOR---
                
                for (int i = 0; i < 5; i++) // same as java
                {
                    //do something
                }


                //---WHILE---

                while(truth) // currently infinite loop
                {
                    //do something
                }

                //---DO WHILE---
                do{

                } while (truth);
                    //do something

            //LOGIC STATEMENTS
                /*
                ---IF ELSE--
                */

                if (truth) 
                {
                    //do something
                } else 
                {
                    //do something else
                }
                    /
                /*
                ---SWITCH---*/ 

                switch (c)
                {
                    case 0:
                        //do something
                        break;
                    case 1: 
                        // do something 
                        break;
                    default:
                        //do something 
                        break;
                }

            //Exception Handling
                try 
                {
                    //risky code
                }
                catch (Exception e) // catches these types of exception
                {
                    //in case of crashing --good for logging errors
                    Console.WriteLine(e.Message);
                }
                finally
                {
                    //this has to run no matter what
                }

        }

        static void Example(string parameter)  // Capitalize all Words
        {
            Console.WriteLine("This is an template for methods in C#");
        }

        static int ReturnEx() // same as java
        {
            return 20;
        }
    }
}