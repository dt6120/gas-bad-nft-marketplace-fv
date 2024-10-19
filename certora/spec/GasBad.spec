using NftMarketplace as nftMarketplace;
using GasBadNftMarketplace as gasBadNftMarketplace;

methods {
    function getListing(address, uint256) external returns INftMarketplace.Listing envfree;
    function getProceeds(address) external returns uint256 envfree;
    function _.safeTransferFrom(address, address, uint256) external => DISPATCHER(true);
    function _.onERC721Received(address, address, uint256, bytes) external => DISPATCHER(true);
}

ghost mathint listingUpdateCounter {
    init_state axiom listingUpdateCounter == 0;
}

ghost mathint log4Counter {
    init_state axiom log4Counter == 0;
}

hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price uint256 price {
    listingUpdateCounter = listingUpdateCounter + 1;
}

hook LOG4(uint256 offset, uint256 length, bytes32 t1, bytes32 t2, bytes32 t3, bytes32 t4) {
    log4Counter = log4Counter + 1;
}

rule sanity(method f) {
    env e;
    calldataarg arg;

    f(e, arg);

    assert listingUpdateCounter <= log4Counter, "counters mismatch";
}

invariant anytime_mapping_updated_emit_event()
    listingUpdateCounter <= log4Counter;

rule calling_any_function_should_result_in_each_contract_having_the_same_state(method f1, method f2)
// filtered {
//     f1 -> f1.selector == f2.selector,
//     f2 -> f2.selector == f1.selector
// }
{
    require f1.selector == f2.selector;

    env e;
    calldataarg args;

    address nftAddress;
    uint256 tokenId;
    address seller;

    require nftMarketplace.getListing(e, nftAddress, tokenId).price == gasBadNftMarketplace.getListing(e, nftAddress, tokenId).price;
    require nftMarketplace.getListing(e, nftAddress, tokenId).seller == gasBadNftMarketplace.getListing(e, nftAddress, tokenId).seller;
    require nftMarketplace.getProceeds(e, seller) == gasBadNftMarketplace.getProceeds(e, seller);

    nftMarketplace.f1(e, args);
    gasBadNftMarketplace.f2(e, args);

    assert nftMarketplace.getListing(e, nftAddress, tokenId).price == gasBadNftMarketplace.getListing(e, nftAddress, tokenId).price, "getListing price mismatch";
    assert nftMarketplace.getListing(e, nftAddress, tokenId).seller == gasBadNftMarketplace.getListing(e, nftAddress, tokenId).seller, "getListing seller mismatch";
    assert nftMarketplace.getProceeds(e, seller) == gasBadNftMarketplace.getProceeds(e, seller), "getProceeds amount mismatch";
}
