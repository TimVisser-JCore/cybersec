Title: Cryptography
Date: 2024-02-09
Summary: Envision cryptography as placing your assets in a secure digital vault, safeguarded by a secret code—your assurance that digital valuables of all sorts remain shielded from prying eyes.

### Mitigates against
- Cryptographic failures
- Vulnerable and outdated components
- Software and data integrity failures

In the intricate tapestry of digital security, encryption emerges as a sentinel, safeguarding sensitive data and fortifying the inner workings of applications. As developers navigate the ever-expanding landscape, it's imperative to not only wield encryption as a shield for user-facing applications but also to weave its protective threads into the fabric of development pipelines and internal systems. Here's a comprehensive guide for individual developers and development teams to master the art of encryption across various facets of their digital citadel.

## User-Facing Applications

For user-facing applications, encryption acts as a steadfast guardian, shielding sensitive user data from prying eyes. Employ robust encryption algorithms and protocols to ensure the confidentiality and integrity of data during transmission and storage. Where possible, use trusted and dependable libraries to handle your cryptographic needs. Cryptography is a highly technical and fragile problem to solve and implementing custom solutions will more than likely result in problems.

## Credential Encryption in Development Pipelines

Credentials are the lifeblood of secure systems, and their encryption should echo resilience. Embrace the concept of immutability by storing credentials in a secure vault and restricting access strictly to automated processes. Avoid hardcoding credentials in source code, configuration files, or version control repositories.

A good place to start with the introduction of cryptography as a strategy for fortifying your environment is your development pipeline. The journey of code from development to deployment traverses various landscapes, and securing this path is paramount. Encrypt credentials used in development pipelines to thwart unauthorized access.

A solution to this could be tools specifically intended to manage credentials within your landscape, e.g.:

- [HashiCorp Vault](https://www.vaultproject.io/) 
- [Cyberark](https://www.cyberark.com/) 

Tools like this - in a general sense - allow you to encrypt and manage sensitive information, ensuring that only authorized entities possess the keys to the kingdom.

Depending on the platforms you are already using, you may even be able to utilise built-in functionality to shield secrets that only your application should be able to access. Most CICD solutions allow the definition of secrets to be used by your application such that credentials your application requires need not be visible after configuring them. Of course - like all solutions - this has its limitations, but can provide a great first line of defense.

## Hashing

Some data is present within systems that is only used to compare against other data, such as in the case of passwords. An application does not need to store the user's password in order to check its validity. This is where hashing comes in. A hashing algorithm is a repeatable, deterministic one-way transformation from a certain input to a storable output. While it is wise to implement ready to use solutions when implementing this, understanding the basics is a valuable addition to your toolkit. Once the input data has been converted to a hash, any future comparisons can be done using only the hashes without having to store the original input. This ensures that actors with access to the hash can not (trivially) obtain the original input (e.g. password). This limits the possibility for attacks like credential stuffing, a significant risk associated with password reuse.

## Internal Systems Protection:

Beyond user data and development pipelines, internal systems house a trove of critical information. When handling sensitive information (e.g. personally identifiable information) it is always wise to consider the implications of this data if it became available to nefarious actors. Data that is not present can also not be stolen, as such it is wise to limit the data you store to only include that which is necessary for the functioning of your application.

Of course, most meaningful applications will eventually have to retrieve, process and/or store sensitive information. In these cases, it's prudent to evaluate which details should receive which protections while making accurate determinations about the trade-offs associated it. Additionally, it is worthwhile to consider the advice contained within the [Access Control]({filename}/access-control.md) topic. Limiting access to those users who explicitly require it and ensuring that this group is as limited as possible is a good strategy in preventing unnecessary risks.

## Continuous Education and Adaptation:

The landscape of encryption evolves, and developers must be agile learners. Staying up to date on the latest encryption algorithms, vulnerabilities, and best practices can be useful but also daunting. As such, a sustainable solution should focus on determining exactly which threats exist in an environment, which data must be protected and setting up automated systems that establish the foundation for a reasonable defense.

## Rigorous Testing:

Encryption is only as strong as its implementation. Subject your encryption mechanisms to rigorous testing. Conduct regular penetration testing, vulnerability assessments, and code reviews to identify and rectify any weaknesses in your cryptographic defenses.

As custodians of digital security, developers bear the responsibility of fortifying the digital citadel against the relentless tides of cyber threats. Encryption, wielded with precision and understanding, becomes an indomitable ally in this quest. By integrating encryption seamlessly into the user-facing realms, development pipelines, and internal systems, developers forge a resilient fortress that stands tall against the challenges of the digital frontier.