// Lines needed to be added in code
System.setProperty("webdriver.chrome.driver","D:\API\chromedriver.exe");

ChromeOptions opt=new ChromeOptions();

opt.setExperimentalOption("debuggerAddress","localhost:9222 ");

WebDriver driver=new ChromeDriver(opt);

driver.get("http://facebook.com");
