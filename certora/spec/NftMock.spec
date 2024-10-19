methods {
    function balanceOf(address) external returns uint256 envfree;
    function totalSupply() external returns uint256 envfree;
    function mint() external;
}

rule minting_mints_one_nft() {
    env e;
    address minter;

    require e.msg.value == 0;
    require e.msg.sender == minter;

    mathint startBalance = balanceOf(minter);

    mint(e);

    assert to_mathint(balanceOf(minter)) == startBalance + 1, "Only 1 NFT should be minted";
}

// invariant totalSupplyIsNotNegative()
//     totalSupply() >= 0;

// rule sanity {
//     satisfy true;
// }

rule total_supply_should_not_change(method f) {
    uint256 totalSupplyBefore = totalSupply();

    env e;
    calldataarg arg;
    f(e, arg);

    assert totalSupply() == totalSupplyBefore, "total supply changed";
}
