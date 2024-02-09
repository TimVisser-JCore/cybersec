Title: Access Control
Date:2024-02-08
Summary: Here's a quick summary about access control

### Mitigates against
- Broken access control

Access control refers to the concept of restricting and allowing access to sensitive resources. We observe this concept from the perspective of the principle of least privilege (PoLP). We want users to have that and only that degree of access that allows them to carry out their responsibilities without significant obstruction. 

With access to sensitive resources comes an inevitable degree of risk. By adhering to PoLP we indicate that we observe this risk and limit its impact to the lowest possible severity.

For our purposes we can broadly distinguish two forms of access control: attribute-based (ABAC) and role-based (RBAC). With attribute-based control, both resources and users have a set of attributes associated with them that are validated against a set of rules that form the bridge between user and resource. Role-based access control, on the other hand, establishes a set of roles that collect a number of permissions. A user can be assigned a set of roles that in turn allows them to access the resources required to satisfy the requirements of their role.

_[ Intuition: RBAC > ABAC for our case, research further to verify ]_  
Maintaining RBAC setup is easier as most administrative load is up-front when defining appropriate roles

Successful and sufficient role-based access control hinges on three separate pillars:  
- Access
- Operations
- Sessions

## Access
Which resources are exposed to the user? In simple terms, this is in reference to everything the user can view.

## Operations
For our purposes we define an operation as any action that retrieves, modifies or otherwise interacts with a resource.

## Session management
This relates to when, for how long and under what conditions the user is allowed to access these resources.

[ Investigate different RBAC variations ? (flat, hierarchical, constrained, symmetric) ]

As different systems have various ways of implementing access control, there is no one-size fits all approach. As such, it should be evaluated how this mitigation can be applied to appropriate systems on a case by case basis.  A good place to start is the team's cloud platform, as this is the core of most operations a development team will be involved in. Safeguarding the resources encompassed by such a platform will have a sizeable impact, especially when combined with proper authentication and authorisation as detailed in [ ref. to auth mitigation ]  

[ Example of RBAC implemented on platform t.b.d.  -> Provide example of implementation in e.g. Spring -> hierarchical roles etc. ]  

[ Section on assigning roles: commutative assignment, four eyes, etc.  -> don't be too specific about lower level considerations ]  

[ Removing unused access? ]  



[ Split between the tools the team uses, and the application(s) the team builds ]  

