using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        public double elapsed = 0;
        public int tcount=0;
        static void Main(string[] args)
        {
            try
            {
                // Start a task - calling an async function in this example
                Stopwatch s = new Stopwatch();
                s.Start();
                //Task<string> callTask = Task.Run(() => CallHttp());
                //// Wait for it to finish
                //callTask.Wait();
                //// Get the result
                //string astr = callTask.Result;
                //string astr = CallHttpSync();
                Program p = new Program();
                Thread g = new Thread(p.testmethod3);
                g.Start();
                Thread ga = new Thread(p.testmethod5);
                ga.Start();
                Thread gb = new Thread(p.testmethod5b);
                gb.Start();
                Thread gc = new Thread(p.testmethod5c);
                gc.Start();
                Thread gd = new Thread(p.testmethod5d);
                gd.Start();
                
                
                //testmethod3();
                //testmethod5();
                //testmethod5b();
                //testmethod5c();
                //testmethod5d();
                // Write it our
                //Console.WriteLine(astr);
                while (p.tcount != 5)
                {
                   
                    
                }
                s.Stop();
                Console.Write("Multi Threaded Elapsed Time {0}", s.Elapsed);
                Console.Write("Single Threaded Elapsed Time {0}", p.elapsed);
                Console.Read();
            }
            catch (Exception ex)  //Exceptions here or in the function will be caught here
            {
                Console.WriteLine("Exception: " + ex.Message);
            }


        }

        //static async Task MultiThread() {
        //    MultiThreadInner();
        //}
        //static void MultiThreadInner()
        //{
        //    Thread g = new Thread(testmethod3);
        //    g.Start();
        //    Thread ga = new Thread(testmethod5);
        //    ga.Start();
        //    Thread gb = new Thread(testmethod5b);
        //    gb.Start();
        //    Thread gc = new Thread(testmethod5c);
        //    gc.Start();
        //    Thread gd = new Thread(testmethod5d);
        //    gd.Start();
            

        //}

         public void testmethod3() {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Thread.Sleep(30000);
            Console.Write("Test 3 method complete");
            sw.Stop();
            elapsed += sw.Elapsed.Seconds;
            tcount += 1;
            
        }

        void testmethod5()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Thread.Sleep(5000);
            Console.Write("Test 5 method complete");
            sw.Stop();
            elapsed += sw.Elapsed.Seconds;
            tcount += 1;
        }
        void testmethod5b()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Thread.Sleep(7000);
            Console.Write("Test 5 method complete");
            sw.Stop();
            elapsed += sw.Elapsed.Seconds;
            tcount += 1;
        }
        void testmethod5c()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Thread.Sleep(6000);
            Console.Write("Test 5 method complete");
            sw.Stop();
            elapsed += sw.Elapsed.Seconds;
            tcount += 1;
        }
        void testmethod5d()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Thread.Sleep(20000);
            Console.Write("Test 5 method complete");
            sw.Stop();
            elapsed += sw.Elapsed.Seconds;
            tcount += 1;
        }
        // Simple async function returning a string...
        static public async Task<string> CallHttp()
        {
            // Just a demo.  Normally my HttpClient is global (see docs)
            HttpClient aClient = new HttpClient();
            // async function call we want to wait on, so wait
            string astr = await aClient.GetStringAsync("http://microsoft.com");
            Thread.Sleep(10000);
            Console.WriteLine(astr);
            // return the value
            return astr;
        }

        static public  string CallHttpSync()
        {
            // Just a demo.  Normally my HttpClient is global (see docs)
            HttpClient aClient = new HttpClient();
            // async function call we want to wait on, so wait
            string astr = aClient.GetStringAsync("http://microsoft.com").Result;
            Console.WriteLine(astr);
            // return the value
            return astr;
        }
    }
}
