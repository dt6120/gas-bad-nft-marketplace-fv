methods {
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
