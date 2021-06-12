//"SPDX-License-Identifier: UNLICENSED"

pragma solidity  ^0.8.4;

contract Flex {

    uint private certificate;
    

    //identifier for O field of cert
    event SendedCertificate(uint indexed certID, bytes32 indexed identifier, string data, uint  expiry);
    event RevokedCertificate(uint indexed certID);

    function sendCertificate(bytes32 identifier, string memory data, uint expiry) public returns (uint certID) {

        certID = certificate++;
        
        emit SendedCertificate(certID,identifier,data,expiry);

        return certID;

    }
    
    function revokeCertificate(uint certID) public returns (uint) {
        require(certificate>certID);
        emit RevokedCertificate(certID);
        return certID;
    }
}