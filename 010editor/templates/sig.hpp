//------------------------------------------------
//--- 010 Editor v13.0.2 Binary Template
//
//      File: 
//   Authors: 
//   Version: 
//   Purpose: 
//  Category: 
// File Mask: 
//  ID Bytes: 
//   History: 
//------------------------------------------------
struct Sig {
    uint16 sz;
};
while (!FEof()) {
   Sig sig;
   FSkip(sig.sz);
}
