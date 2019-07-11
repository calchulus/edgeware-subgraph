# Edgeware-subgraph
[Edgeware](https://edgewa.re/) is a parachain built on Polkadot that is conducting a lock drop using Ethereum. This [Subgraph](https://thegraph.com/explorer/subgraph/calchulus/edgeware-lockdrop) takes in the first contract of the Lockdrop for the protocol. See [here](https://thegraph.com/explorer/subgraph/calchulus/edgewarelockdroptwo) for the latest second contract (locks are still currently occurring), and another testnet contract [here](https://thegraph.com/explorer/subgraph/calchulus/testnet-edgeware) 

For ABIs and other downloads related to the other two contracts (EdgewareLockdrop2 & Testnet), please click into their respective folders in this repo. 

## Networks and Performance

This subgraph can be found on The Graph Hosted Service at https://thegraph.com/explorer/subgraph/calchulus/edgeware-lockdrop

You can also run this subgraph locally, if you wish. Instructions for that can be found in [The Graph Documentation](https://thegraph.com/docs/quick-start). 

## Contract Upgrades

I will need to learn how to bundle multiple contracts into one graph, as I ended up submitting a separate subgraph for each contract of Edgeware.the most recent subgraph. 

## Getting started with querying 
Below are a few ways to show how to query the Edgeware Subgraphs for data. The queries show most of the information that is queryable, but there are many other filtering options that can be used, just check out the [querying api](https://github.com/graphprotocol/graph-node/blob/master/docs/graphql-api.md).


### Querying Mainnet Contract ### Lockers The following query can be used to find the largest lockers in the Lockdrop. Note, this cannot be done for signaled, as signaleds have different parameters. More on them later. 

```graphql
{ lockeds(orderDirection: desc, orderBy: eth) {
    id
    owner
    eth
    lockAddr
  }
}

```
The orderDirection allows for the largest, and the orderBy allows the Eth to be the item to sort by. Note, this only returns the top 100 results.

 Some future ideas of other things to look at include “repeat” Lockers, if any owner is a repeat of a previous locker. Pagination is also interesting - more on that later.
### Signaleds
Signalers have no incentive in the lock drop to signal early, but those who do early are very sold on wanting to participate, so time is very relevant. Thus, a nice query could be something like:
```graphql
{
 signaleds(first: 100) {
    id
    contractAddr
    edgewareAddr
    time
  }
}
```
This would retrieve the first 100 participants, the zealous bunch who have participated.

###Pagination
Want to query this graph to get all of the signalers or lockers? To get around the limitations of only the top 100 for the Lockers or the first 100 signalers, just add the skip parameter prior to querying the “first” or the ordered lockers. 
```graphql
{
 signaleds(skip:100, first:100) {
    id
    contractAddr
    edgewareAddr
    time
  }
}
```

###Unique Takeaways

Active ropsten addresses - these guys are testing out things on chains and have good operational safety

A next step would be to compare these ropsten addresses to if these addresses have any mainnet ETH in the same address - this would suggest potential signalers or lockers who have yet to participate but have already done preparatory work to get ready for participation.

It would also mean that these testers might be interested in some sort of similar mechanism, such as https://straighted.ge. It would be a very neat targeted ad campaign to send testnet tokens on Ropsten to these folks to see if they would try out your project, at no cost to the sender.

### Python
The jsons returned from the data are really nice and easy to work with in python. I’ve included a couple sample jsons returned from this subGraph & have given a quick and dirty Python Script to allow one to return address lists, amounts, etc.

Love how flexible all this data is! So easy to query.

### Challenges

I tried forking the EThDenver Template Dapp but man, I had a lot of issues refactoring it. I just gave up and created a quick and dirty selector to bundle access to all three Edgeware contracts, and then provide some of the sample queries for users to try themselves. 

### Next steps
I would love to do more analysis on the “Poisson point arrival” process of participants in the lock drop to model out how much participation occurs at the end of the “time windows” for various bonuses on the lock drop, as anecdotally there were many last second deposits, as displayed in the Commonwealth stats page. It would be very neat to model the time intervals between lockdrop participants, and the time field in this subgraph is super easy to query :) 

