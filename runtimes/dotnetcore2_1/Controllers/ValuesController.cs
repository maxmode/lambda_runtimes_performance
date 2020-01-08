using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace exampleservice.Controllers
{
    [Route("dotnet2.1")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        // GET dotnet2.1
        [HttpGet]
        public ActionResult<string> Get()
        {
            return "Hello from Lambda!";
        }
    }
}
