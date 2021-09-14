using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Something
{
    class CheatObjectsandClass
    {
        public string field1; // characteristic of the object
        public static int num; // static -- characteristic of the class
        
        public CheatObjectsandClass(string someparameter, int num){
            //do something
            this.field1 = someparameter;
            this.num = num;
            //set defaults
        }

        public string GetandSet()
        {
            get { return field1; }
            set { 
                //set rules here
                if (value) //follows some condition
                {       field1 = value;
                } else 
                {
                    field1 = null;
                }
                
            }
        }

        public static int QuickTasks
        {
            return 6+
        }

        public bool PrintSmile()
        {
            Console.WriteLine(":)")
        }
    }
}