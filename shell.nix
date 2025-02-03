{ pkgs ? import <nixpkgs> {} }:
let
  my-python = pkgs.python3;
  python-with-my-packages = my-python.withPackages (p: with p; [
    pygments
    # add more needed python packages here
  ]);

  my-texlive = pkgs.texlive.combine { 
    inherit (pkgs.texlive) 
    scheme-medium

    preprint
    catchfile
    comment
    environ
    framed
    fvextra
    hyperxmp
    ifmtarg
    lipsum
    marginnote
    minted
    ncctools
    pygmentex
    todonotes
    totpages
    upquote
    xargs
    xifthen
    xstring

    # add more needed texlive packages here
    ; 
  };
in
pkgs.mkShell {
  name = "opencompl";

  packages = [
    python-with-my-packages
    # include this if you wish to run --pure shells, otherwise save you the trouble and use your texlive scheme-full system installation
    # my-texlive

    # "normal dependencies"
    pkgs.python3
    pkgs.gnumake
    pkgs.which
  ];
}
