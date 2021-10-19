using Microsoft.Online.SharePoint.TenantManagement;
using Microsoft.ProjectServer.Client;
using Microsoft.SharePoint.Client;
using Microsoft.SharePoint.Client.Publishing;
using System;
using System.Linq;
using System.Security;
using System.Text;
using System.Threading;

namespace AddNewItemsToAbsences
{

    class Program
    {
        private static string _User = "";
        private static string _Password = "";
        private static string _SiteUrl = "https://rbcom.sharepoint.com/sites/AnnualLeaveTrackerDev";


        static void Main(string[] args)
        {
            var pwdS = new SecureString();
            foreach (var c in _Password.ToCharArray()) pwdS.AppendChar(c);
            var ctx = new ClientContext(_SiteUrl) { Credentials = new SharePointOnlineCredentials(_User, pwdS) };
            AddNewItem(ctx);
            Console.ReadKey();
        }

        //GENERATE RANDOM VALUE
        private static string CreateRandomString()
        {
            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            var stringChars = new char[8];
            var random = new Random();
            for (int i = 0; i < stringChars.Length; i++)
            {
                stringChars[i] = chars[random.Next(chars.Length)];
            }
            return new string(stringChars);
        }

        //GENERATE RANDOM DATE
        private static string RandomDate(int startYear = 2020, string outputDateFormat = "yyyy-MM-dd")
        {
            DateTime start = new DateTime(startYear, 1, 1);
            Random gen = new Random(Guid.NewGuid().GetHashCode());
            int range = (DateTime.Today - start).Days;
            return start.AddDays(gen.Next(range)).ToString(outputDateFormat);
        }



        private static void AddNewItem(ClientContext ctx)
        {
            Console.WriteLine($"New item added");
            try
            {
                var list = ctx.Web.Lists.GetByTitle("Absences");
                ctx.Load(list);
                ctx.ExecuteQuery();
                ListItemCreationInformation ItmCreationInfo = new ListItemCreationInformation();
                var counter = 0;

                for (int i = 0; i < 2; i++)
                {
                    var randomString = CreateRandomString();
                    var randomDate = RandomDate();
                    //string emailUser = Convert.ToString("Sp10gammatest2@RBcom.onmicrosoft.com");

                    var myItem = list.AddItem(ItmCreationInfo);
                    //UPDATE PERSON OR GROUP FIELD ("APPROVER")
                    string testName = "userEmailAddress"; //use display name instead of login name  
                    if (testName != "")
                    {
                        User userTest = ctx.Web.EnsureUser(testName);
                        ctx.Load(userTest);
                        ctx.ExecuteQuery();
                        testName = userTest.Id.ToString() + ";#" + userTest.LoginName.ToString();

                        myItem["Approver"] = testName;
                    }
                    //item.Update();
                    //context.ExecuteQuery();
                    //myItem["Approver"] =
                    myItem["StartDate"] = randomDate;
                    myItem["EndDate"] = randomDate;
                    myItem["Title"] = "useremailaddressUsedToLogin";
                    myItem["LeaveType"] = "Annual Leave";
                    myItem["Status"] = "Pending";
                    myItem["Year"] = "2020";
                    myItem["DaysCount"] = 1;


                    myItem.UpdateOverwriteVersion();
                    ctx.ExecuteQuery();
                    Console.WriteLine(i);
                    //Wait 1s after adding every 100 items
                    counter++;
                    if (counter == 100)
                    {
                        Thread.Sleep(1000);
                        counter = 0;
                    }
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine($"[ERROR] {ex.Message}");
            }
        }
    }
}