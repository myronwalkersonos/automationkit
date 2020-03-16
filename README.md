# Automation Kit Repository

Welcome to the Automation Kit repository!

# Description
The **Automation Kit** is a python toolkit for building distributed automated task and testing systems.  It goes beyond the capabilities of other task and test automation frameworks by providing an object oriented framework that can be utilized to easily customize the orchestration of tasks and tests across a collection of integrated resources.  Because the **Automation Kit** is built from the start with distributed automation in mind, it can help you quickly get distributed automated systems up and running quickly that are based on a tested and proven set of object patterns and APIs.

# Design Philosophies
This section covers some of the important design features of the **Automation Kit** framework.

## Large Scale
The **Automation Kit** is designed for enterprise level distributed automation *"at scale"*.  The term *"at scale"* refers not only to a larger collection of enterprise resources but also refers to the fact that the **Automation Kit** helps to setup patterns that will support working in a very large code base.  The size of a code base that you might see associated with large enterprise level projects.  The **Automation Kit** support working in large code bases by helping to establish good code organizational patterns and abstractions that support characteristics that:

* make is easier to learn and work in the code base
* make the code base easier to maintain
* make it easier to share and reuse code

## Faster Classification of Issues
One of the key philosophies behind the **Automation Kit** design is one of being able quickly and efficiently identify the nature of issues that come up during automation runs.  The **Automation Kit* initially classifies errors into one of four categories:

* **Configuration** - We identify configuration issues quickly and classify the so as configuration related issues so as to ensure that we don't waist time troubleshooting configuration related issues.
* **Environment** - The **Automation Kit** performs an initial diagnostic scan of the automation landscape and all the resources declared to be necessary to run a series of tasks or tests in order to provide indications of environmental failures as early as possible.  This is important to ensure that we do not generate noise in automation results that are not related to the automation tasks or tests that might fail.
* **Error** - The **Automation Kit** classifies un-expected errors or errors that are not founded in an expectation of a result as an **Error** condition.  This helps to ensure these errors are given an appropriate initial direction or indication that the issues is a problem in the automation code and not an issue in the code that is the target of the automation run.
* **Failure** - The **AutomationKit** classifies failures that are associated with an expectation of behavior from a target under test as failures.  This allows for the proper initial classification of an issue as being a problem that is likely failure in the target of the automation and the behavior or result it should have exhibited.

Having the initial classification of issues fall into one of these four categories helps to ensure that issues are easier to triage and assign to the appropriate party for investigation and resolution.

## Integration and Distributed Automation Support
The **Automation Kit** comes with enterprise level integration and distributed automation capabilities.  The framework utilizes a customize-able set of classes that guides enterprise users through a process of creating a very robust integration object model based on the roles that enterprise resources play in an automation landscape.

The declaration of custom automation landscape is as simple as setting a environment variable or passing a command line flag declaring the python module the custom landscape derived class.  The *Landscape* and *LandscapeDescription* derived classes work together to provide the **Automation Kit** with a description of the customized roles and integration mixin(s) that provide the connection between the tasks and test automation code.

## Task and Test Integration Declaration and Assurance
The **Automation Kit** utilizes its object model to allow tasks and tests to provide information about their associated integration points and scopes of execution to that automation framework.  This integration declaration mechanism allows the automation framework to provide an early scan of the integration pathways and provide levels of assurance as to the stability of the automation landscape early in the automation process.  This is vitally important as it eliminates the waist and noise that are often associated with automation runs that are performed against an automation Landscape that has broken, mis-configured or missing resources.

## Automation Job, Scope and Flow Control 
The **Automation Kit** allows enterprise users to organize and customize the ordering of automation scope engagements and the flow of an automation job.  This provide the automation engineer the ability to control the engagement of automation scopes of execution and allows for optimal use of time and overlapping of scopes of execution in a test run.

