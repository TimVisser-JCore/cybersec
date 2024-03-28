Title: Scanning
Date: 2024-02-09
Summary: Your project's vigilant guardian. Regular scans of your projects, environment and credentials can allow you to fortify your digital assets against threats. 

### Mitigates against
- Broken access control 
- Insecure design
- Vulnerable and outdated components 
- Security misconfigurations

In software development we often deal with a highly complex landscape of innumerable dependencies and tools that are interconnected to eventually provide some sort of functionality that is the intended purpose of an application. In this process, it's easy to lose sight of the finer details of an implementation. Maintaining this overview manually would be a herculean task, and as developers we'd rather be focused on providing value to the user than carrying out janitorial tasks to maintain our applications. This is where automated scanning comes in. In this topic, we will touch on a number of scanning types and some of its intricacies.

## Credential Scanning

Credentials are the keys to the digital kingdom, and their security is paramount. Developers, embrace credential scanning practices to detect exposed or compromised credentials. Although by no means a best practice, during development it may happen that credentials sneak into the codebase with potentially disastrous results when these credentials leak outside the scope of its intended owners. We can limit the risk associated with this threat vector using credential scanners. While numerous solutions exist, a good place to start may be:

- [SAP Credential-Digger](https://github.com/SAP/credential-digger)
- [GitGuardian](https://www.gitguardian.com/)

At a basic level, these tools work by scanning your codebase on new additions to determine the presence of live credentials. Quality gates may be set up (as discussed in the [Cyber Hygiene]({filename}/cyber-hygiene.md)) topic to enforce the amendment of a contribution to the codebase when credentials are detected where they should not be present.

## Vulnerability Scanning

Every line of code holds the potential for vulnerabilities. Integrate vulnerability scanning tools into the development pipeline to systematically identify and address weaknesses. Regular scans unveil the vulnerabilities that might be exploited by malicious actors, fortifying the application against potential breaches. This subject is largely discussed in the [Cyber Hygiene]({filename}/cyber-hygiene.md) topic.

## Dependency Scanning

The software ecosystem is a tapestry woven with dependencies, each thread carrying its own risks. Employ dependency scanning tools to scrutinize libraries, frameworks, and third-party components for known vulnerabilities. This practice ensures that every strand in the digital tapestry is resilient, guarding against the vulnerabilities that may reside in the shadows. The [Cyber Hygiene]({filename}/cyber-hygiene.md) topic goes into further detail about this form of scanning.

## Code Quality Scanning

The quality of code is the cornerstone of robust applications. Embrace code quality scanning tools that assess adherence to coding standards, identify potential bugs, and enforce best practices. A well-orchestrated code quality scan ensures that the composition of your digital landscape remains elegant and error-free. While a large number of solutions for this exist, a good place to start is the solutions provided by [SonarQube](https://www.sonarsource.com/products/sonarqube/).

Good metrics to focus on (in addition to many others) depend on the team and its requirements, but a good place to start would be test coverage, complexity and code smells. SonarQube can also be used to fulfill several of the recommendations made in the [Cyber Hygiene]({filename}/cyber-hygiene.md) topic.

## Regular audits and compliance

While not the main topic of this guide, some consideration may be given to compliance needs of the industry the team operates 

In the grand overture of software development, where each line of code contributes to the composition, scanning emerges as the vigilant conductor, harmonizing the defense against potential vulnerabilities and threats. Developers, heed the melodies of scanning with precision, for it is in the orchestrated interplay of scans that the security of digital landscapes finds its strength and resilience.