
<?xml version="1.0" encoding="utf-8"?>

<configuration>

	<system.web>
		<monoSettings>
			<compilersCompatibility>
				<compiler language="c#;cs;csharp" extension=".cs" compilerOptions="/nowarn:0169"
					  type="Microsoft.CSharp.CSharpCodeProvider, System, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
			</compilersCompatibility>
		</monoSettings>
		
		<authorization>
			<allow users="*" />
		</authorization>
		<httpHandlers>
			<add verb="*" path="Trace.axd" type="System.Web.Handlers.TraceHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="UrlRouting.axd" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.aspx" type="System.Web.UI.PageHandlerFactory, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.asmx" validate="false" type="System.Web.Services.Protocols.WebServiceHandlerFactory, System.Web.Services, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.ashx" type="System.Web.UI.SimpleHandlerFactory, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="GET" path="WebResource.axd" type="System.Web.Handlers.AssemblyResourceLoader, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.master" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.resources" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.skin" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.browser" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.sitemap" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.webinfo" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.resx" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.asax" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.ascx" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.config" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.Config" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.cs" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.vb" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.csproj" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.vbproj" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.licx" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.dll" type="System.Web.HttpForbiddenHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*.rem" type="System.Runtime.Remoting.Channels.Http.HttpRemotingHandlerFactory, System.Runtime.Remoting, Culture=neutral, PublicKeyToken=b77a5c561934e089" validate="false" />
			<add verb="*" path="*.soap" type="System.Runtime.Remoting.Channels.Http.HttpRemotingHandlerFactory, System.Runtime.Remoting, Culture=neutral, PublicKeyToken=b77a5c561934e089" validate="false" />
			<add verb="*" path="*.svc" type="System.ServiceModel.Channels.SvcHttpHandlerFactory, System.ServiceModel, Version=3.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
			<add verb="GET,HEAD" path="*" type="System.Web.StaticFileHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add verb="*" path="*" type="System.Web.HttpMethodNotAllowedHandler, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
		</httpHandlers>
		<httpModules>
			<add name="FormsAuthentication" type="System.Web.Security.FormsAuthenticationModule, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add name="OutputCache" type="System.Web.Caching.OutputCacheModule, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add name="RoleManager" type="System.Web.Security.RoleManagerModule, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add name="Session" type="System.Web.SessionState.SessionStateModule, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			<add name="UrlAuthorization" type="System.Web.Security.UrlAuthorizationModule, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
		</httpModules>
		<authentication mode="Forms">
			<forms name=".MONOAUTH" loginUrl="login.aspx" protection="All" timeout="30" path="/">
				<credentials passwordFormat="Clear">
					<!--<user name="gonzalo" password="gonz"/>-->
				</credentials>
			</forms>
		</authentication>
		<machineKey validationKey="AutoGenerate" decryptionKey="AutoGenerate" validation="SHA1" />
		<globalization  requestEncoding="utf-8"
				responseEncoding="utf-8"
				fileEncoding="utf-8"/>
		<!--
				culture="en-US"
				uiculture="en-US" />
		-->
		<sessionState mode="InProc" />
		<pages>
        		<namespaces>
            			<add namespace="System" />
            			<add namespace="System.Collections" />
            			<add namespace="System.Collections.Specialized" />
            			<add namespace="System.Configuration" />
            			<add namespace="System.Text" />
            			<add namespace="System.Text.RegularExpressions" />
            			<add namespace="System.Web" />
            			<add namespace="System.Web.Caching" />
            			<add namespace="System.Web.SessionState" />
            			<add namespace="System.Web.Security" />
            			<add namespace="System.Web.Profile" />
            			<add namespace="System.Web.UI" />
            			<add namespace="System.Web.UI.WebControls" />
            			<!-- <add namespace="System.Web.UI.WebControls.WebParts" /> -->
            			<add namespace="System.Web.UI.HtmlControls" />
        		</namespaces>
    		</pages>
		<webControls clientScriptsLocation="/web_scripts" />
		<compilation debug="false" defaultLanguage="c#" explicit="true" strict="false" >
			<assemblies>
				<!--<add assembly="mscorlib" /> -->
				<add assembly="System, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            			<add assembly="System.Configuration, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            			<add assembly="System.Data, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            			<add assembly="System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            			<add assembly="System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            			<add assembly="System.Web.Services, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
				<add assembly="System.Runtime.Serialization, Version=3.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, processorArchitecture=MSIL"/>
				<add assembly="System.IdentityModel, Version=3.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, processorArchitecture=MSIL"/>
				<add assembly="System.ServiceModel, Version=3.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"/>
				<add assembly="System.ServiceModel.Web, Version=3.5.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"/>
            			<add assembly="System.Xml, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
				<add assembly="*" /> <!-- Add assemblies in bin directory -->
			</assemblies>
			<expressionBuilders>
				<add expressionPrefix="Resources"
				     type="System.Web.Compilation.ResourceExpressionBuilder, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
				<add expressionPrefix="ConnectionStrings"
				     type="System.Web.Compilation.ConnectionStringsExpressionBuilder, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
				<add expressionPrefix="AppSettings"
				     type="System.Web.Compilation.AppSettingsExpressionBuilder, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
			</expressionBuilders>
			<buildProviders>
				<add extension=".aspx" type="System.Web.Compilation.PageBuildProvider" />
				<add extension=".ascx" type="System.Web.Compilation.UserControlBuildProvider" />
				<add extension=".master" type="System.Web.Compilation.MasterPageBuildProvider" />
				<add extension=".asmx" type="System.Web.Compilation.WebServiceBuildProvider" />
				<add extension=".ashx" type="System.Web.Compilation.WebHandlerBuildProvider" />
				<add extension=".soap" type="System.Web.Compilation.WebServiceBuildProvider" />
				<add extension=".resx" type="System.Web.Compilation.ResXBuildProvider" />
				<add extension=".resources" type="System.Web.Compilation.ResourcesBuildProvider" />
				<add extension=".wsdl" type="System.Web.Compilation.WsdlBuildProvider" />
				<add extension=".xsd" type="System.Web.Compilation.XsdBuildProvider" />
				<add extension=".js" type="System.Web.Compilation.ForceCopyBuildProvider" />
				<add extension=".lic" type="System.Web.Compilation.IgnoreFileBuildProvider" />
				<add extension=".licx" type="System.Web.Compilation.IgnoreFileBuildProvider" />
				<add extension=".exclude" type="System.Web.Compilation.IgnoreFileBuildProvider" />
				<add extension=".refresh" type="System.Web.Compilation.IgnoreFileBuildProvider" />
			</buildProviders>
		</compilation>
		<httpRuntime executionTimeout="110"
			     maxRequestLength="4096"
			     useFullyQualifiedRedirectUrl="false"
			     minFreeThreads="8"
			     minLocalRequestFreeThreads="4"
			     appRequestQueueLimit="5000" />
		<clientTarget>
			<add alias="ie5" userAgent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 4.0)" />
			<add alias="ie4" userAgent="Mozilla/4.0 (compatible; MSIE 4.0; Windows NT 4.0)" />
			<add alias="uplevel" userAgent="Mozilla/4.0 (compatible; MSIE 4.0; Windows NT 4.0)" />
			<add alias="downlevel" userAgent="Unknown" />
		</clientTarget>

		<siteMap>
			<providers>
				<add name="AspNetXmlSiteMapProvider"
				 description="Default site map provider that reads in .sitemap xml files."
				 type="System.Web.XmlSiteMapProvider, System.Web, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
				 siteMapFile="Web.sitemap" />
			</providers>
		</siteMap>
	</system.web>

</configuration>
