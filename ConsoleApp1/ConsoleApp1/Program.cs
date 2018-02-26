using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Reflection;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Prometheus;
namespace ConsoleApp1
{
    class Program
    {
        public double elapsed = 0;
        public int tcount=0;
        const int NUMBER_Of_FILES = 5000;
        static void Main(string[] args)
        {
            try
            {
                // Start a task - calling an async function in this example
                Thread.Sleep(2000);
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
                var counter = Prometheus.Metrics.CreateGauge("Gconsole", "Gconsole", "label");
                var metricServer = new MetricServer(port: 1233);
                metricServer.Start();
                Random r = new Random();
                for (int i = 1; i < 10000; i++)
                {
                    if (i % 2 == 0)
                    {
                        counter.Inc(r.NextDouble()*i);
                    }
                    else
                    {
                        counter.Dec(r.NextDouble()*i);
                    }
                    Thread.Sleep(250);
                }
                Console.Read();    

                //testmethod3();
                //testmethod5();
                //testmethod5b();
                //testmethod5c();
                //testmethod5d();
                // Writeline it our
                //Console.WritelineLine(astr);
                while (p.tcount != 5)
                {
                    //Console.WriteLine(s.ElapsedMilliseconds);
                    
                }
                s.Stop();
                Console.WriteLine("Multi Threaded Elapsed Time {0}", s.ElapsedMilliseconds);
                Console.WriteLine("Single Threaded Elapsed Time {0}", p.elapsed);
                Console.WriteLine("% difference {0} to create {1} files", s.ElapsedMilliseconds*100/p.elapsed, NUMBER_Of_FILES*5);
                Console.WriteLine("per file creation time {0} ", s.ElapsedMilliseconds*1.0 / (NUMBER_Of_FILES * 5));
                Console.Read();
            }
            catch (Exception ex)  //Exceptions here or in the function will be caught here
            {
                Console.WriteLine("Exception: " + ex.Message);
            }


        }

        private static object Metrics()
        {
            throw new NotImplementedException();
        }

        public void testmethod3() {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Task<int> x = CreateManyFiles("testmethod3", NUMBER_Of_FILES);
            x.Wait();
            sw.Stop();
            elapsed += sw.ElapsedMilliseconds;
            tcount += 1;
            
        }

        void testmethod5()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Task<int> x = CreateManyFiles("testmethod5", NUMBER_Of_FILES);
            x.Wait();
            Console.WriteLine("Test 5 method complete");
            sw.Stop();
            elapsed += sw.ElapsedMilliseconds;
            tcount += 1;
        }
        void testmethod5b()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Task<int> x = CreateManyFiles("testmethod5b", NUMBER_Of_FILES);
            x.Wait();
            Console.WriteLine("Test methond 5 b complete");
            sw.Stop();
            elapsed += sw.ElapsedMilliseconds;
            tcount += 1;
        }
        void testmethod5c()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Task<int> x = CreateManyFiles("testmethod5c", NUMBER_Of_FILES);
            x.Wait();
            Console.WriteLine("Test 5 method complete");
            sw.Stop();
            elapsed += sw.ElapsedMilliseconds;
            tcount += 1;
        }
         void testmethod5d()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Task<int> x = CreateManyFiles("testmethod5d", NUMBER_Of_FILES);
            x.Wait();
            Console.WriteLine("Test 5 method complete");
            sw.Stop();
            elapsed += sw.ElapsedMilliseconds;
            tcount += 1;
        }

        async Task<int> CreateManyFiles(string directorypath,int numberoffiles)
        {
            int i = 0;
            if (!System.IO.Directory.Exists(System.IO.Path.Combine(Directory.GetCurrentDirectory(), directorypath)))
            {
               System.IO.Directory.CreateDirectory(System.IO.Path.Combine(Directory.GetCurrentDirectory(), directorypath));
            }
            while (i < numberoffiles)
            {
                string pathString = System.IO.Path.Combine(Directory.GetCurrentDirectory(), directorypath,System.IO.Path.GetRandomFileName() + "----3");
                 await Task.Run(() => System.IO.File.Create(pathString));
                i++;
            }
             return 0;
        }
        
    // Simple async function returning a string...
    static public async Task<string> CallHttp()
        {
            // Just a demo.  Normally my HttpClient is global (see docs)
            HttpClient aClient = new HttpClient();
            // async function call we want to wait on, so wait
            string astr = await aClient.GetStringAsync("http://microsoft.com");
            Thread.Sleep(1000);
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
