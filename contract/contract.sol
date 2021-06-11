//"SPDX-License-Identifier: UNLICENSED"

pragma solidity  ^0.8.5;

contract Flex {

    uint private certificate;
    

    //identifier for O field of cert
    event AddedCertificate(uint indexed certID, bytes32 indexed identifier, string data, uint  expiry);
    event RevokedCertificate(uint indexed certID);

    function addAttribute(bytes32 identifier, string memory data, uint expiry) public returns (uint certID) {

        certID = certificate++;
        
        emit AddedCertificate(uint indexed certID, bytes32 indexed identifier, string data, uint  expiry);

        return certID;

    }
    
    function revokeSignature(uint certID) public returns (uint certID) {
        require(attributes>=attributeID);
        emit RevokedCertificate(uint indexed certID);
        return certID;
    }
}