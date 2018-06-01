using Newtonsoft.Json.Linq;
using System;
using System.Collections;
using System.Collections.Generic;

namespace ConsoleApp2
{

    class Indexer
    {
        private string firstname;
        private string lastname;
        public string name;
        public string this[int index]
        {
            get { return name.Split(" ")[index]; }
        }

        public void print()
        {

            Console.WriteLine(firstname + ":" + lastname);
            Console.ReadKey();
        }

        public IEnumerable<int> listobject()
        {
            for (int i = 0; i < 10; i++)
            {
                //Console.WriteLine("Inside method");
                yield return i;

            }

        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Press key 0 for RateLimit and any other for others ");
            ConsoleKeyInfo option = Console.ReadKey();
            switch (option.KeyChar) {
                case '0':
                    Console.WriteLine("Entering Ratelimit");
                    Ratelimit();
                    break;
                case '1':
                    Console.WriteLine("Entering Hashset");
                    PlayWithHashSet();
                    break;
                case '2':
                    Console.WriteLine("Entering Hashtable");
                    PlayWithHashTable();
                    break;
                case '3':
                    Console.WriteLine("Entering PremCombi");

                    foreach(Tuple<int,int> t in PlayPremutation(new HashSet<int>() { 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18 }))
                    {
                        Console.WriteLine(t.Item1 +":"+ t.Item2);
                       
                    }
                    Console.ReadKey();
                    break;

                case '4':
                    Console.WriteLine("Indexer on class");
                    Indexer i = new Indexer();
                    i.name = "The quick brown fox jumps over the lazy little dog";
                    Console.WriteLine(i[4]);
                    Console.ReadKey();
                    break;
                case '5':
                    Console.WriteLine("Yield example");
                    Indexer l = new Indexer();
                    foreach (int k in l.listobject())
                    {
                        Console.WriteLine(k);

                    }
                    Console.ReadKey();
                    break;
            }

        }

        static HashSet<Tuple<int,int>> PlayPremutation(HashSet<int> h)
        {
            HashSet<Tuple<int, int>> result = new HashSet<Tuple<int, int>>();
            foreach (int i in h)
            {
                foreach(int j in h)
                {
                    result.Add(new Tuple<int, int>(i, j));
                }

            }
            return result;
        }
        static void PlayWithHashTable()
        {
            
            Hashtable k = new Hashtable();
            k.Add(1, 1);
            k.Add(11, 45);
            Console.WriteLine(k[1].GetHashCode());
            Console.WriteLine(k[11].GetHashCode());
            Console.ReadKey();

        }
        static void PlayWithHashSet()
        {
            HashSet<int> j = new HashSet<int>();
            j.Add(5);
            j.Add(5);
            j.Add(6);
            foreach (int i in j)
            {
                Console.WriteLine(i);

            }
            
            Console.ReadKey();
        }
        static void Ratelimit()
        {
            Hashtable hashtable = new Hashtable();
            const int RATELIMIT = 9;
            const int RATEDURATION = 10;


            ConsoleKeyInfo j = Console.ReadKey();
            while (j.KeyChar != '0')
            {
                if (hashtable.ContainsKey(j))
                {
                    JObject jobject = new JObject();
                    jobject = (JObject)hashtable[j];
                    var h = DateTime.Now - jobject["time"].ToObject<DateTime>();
                    if (jobject["count"].ToObject<int>() > RATELIMIT)
                    {

                        if (h.TotalSeconds > RATEDURATION)
                        {
                            jobject["count"] = 1;
                            jobject["time"] = DateTime.Now;
                            hashtable[j] = jobject;
                        }
                        else
                        {
                            Console.WriteLine("Reached Maximum rate for allowed time, try after some time " + h.TotalSeconds);
                        }

                    }
                    else
                    {

                        jobject["count"] = ((JObject)(hashtable[j]))["count"].ToObject<int>() + 1;
                        //jobject["time"]= DateTime.Now;

                        hashtable[j] = jobject;
                        Console.WriteLine("Updated");
                    }

                }
                else
                {
                    JObject jobject = new JObject();
                    jobject.Add("count", 1);
                    jobject.Add("time", DateTime.Now);
                    hashtable.Add(j, jobject);
                    Console.WriteLine("Added");

                }
                j = Console.ReadKey();
                foreach (var key in hashtable.Keys)
                {
                    Console.WriteLine(String.Format("{0}: {1}", ((ConsoleKeyInfo)key).KeyChar, hashtable[key]));
                }
            }

        }
    }
}
