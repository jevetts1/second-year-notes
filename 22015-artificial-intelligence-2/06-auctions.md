# Auctions

Auctions are a model for resource allocation. This allows resources to be distributed among competed agents. 

## Mechanism design

The goal is to design the rules so that the strategic behaviour of participants leads to a desirable outcome for the creator.

This is also called reverse game theory. 
- Convention: truth telling is a dominant strategy
- Dominant strategy incentive compatibility

## Auctions

Scenario 1: single item auction
- One auctioneer, 1 item
- $n$ bidders, each has a value on the item
- how do you sell it to maximise revenue/welfare?

Scenario 2: multi item auction
- One auctioneer, multiple items
- $n$ bidders, each has value on the items
- how do you sell them to maximise revenue/welfare?

Scenario 3
- Selling advertisements on the internet

Procurement auction is one bidder, multiple auctioneers. 

### Single item Auctions

There are four classical auction models for a single item:
- English Auction
- Dutch Auction
- Sealed-bid first price Auction
- Sealed-bid second price Auction

#### English Auction

The most common type of auction.

It is an ascending open bid auction. 
- The price only goes up.
- Everyone can see what the current bid is
- Auctioneer sells to the bidder once no one else bids higher.

There is a dominant strategy to bid the minimum increment value if you aren't winning until the price surpasses your value. 

The items is always sold to the bidder with the highest item value when using the "increase little by little" bid strategy.

#### Dutch Auction

This is also an open bid auction, but the price descends. The auctioneer starts with a high price and drops it down until someone bids for it. 
- First person who bids wins

You could win by bidding once the value is lower to equal to your item value. 

The bidder with the highest value doesn't necessarily win, and the auctioneer does not necessarily get max revenue.

#### Sealed-bid first price Auction

Blind auction:
- Bids submitted in a sealed manner
- Give the item to the agent with the higest bid

The best strategy is to try to guess the second highest bid and then bid slightly higher than that. 

There is no dominant strategy still.

Let's say the agents utility is quasi-linear:
- $u = v - p$ if winning, where $v$ is the value and $p$ is how much the agent paid
- $u = 0$ if losing. 
- *this is quasi-linear because $v$ and $p$ are in different units (scalar for $v$ and money for $p$)*
- The agent can estimate the highest bid is a normal distribution $U(10, 40)$
- So for a bid price $b$,:
    - $E[u] = P(win) \times (v - p) = \frac {b-10} {40-10} \times (30 - b)$
    - Find $\frac {dE[u]} {db} = 0$ to find $b = 20$. This is the best strategy, according to the agent's guess.  

Question:

$v = 50$, distribution is $U(20,100)$.

$$E[u] = P(win) \times (v-p)$$

$$E[u] = \frac {b - 20} {100 - 20} \times (50 - b) = (b/80 - 1/4)(50 - b)$$

$$E[u] = \frac {7}{8} b - \frac {25}{2} - \frac {b^2}{80}$$

$$\frac {dE[u]} {db} = \frac {7}{8} - \frac {b}{40}$$

$$\frac {7}{8} - \frac {b}{40} = 0 \to b = 35$$

#### Sealed-bid second price Auction

Also known as the Vickrey auction. Bids are submitted sealed, and the agent with the highest bid wins, but only pays the **second** highest price. 

The best strategy is always to bid your private value truthfully, because your minimum utility is then 0. **This is a dominant strategy**.

Bidding truthfully is the act of bidding your private value. 