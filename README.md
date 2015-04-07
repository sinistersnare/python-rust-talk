# Python + Rust == Good #

To build:

```bash
$ git clone https://github.com/sinistersnare/python-rust-talk
$ cd python-rust-talk
$ cargo build --release
$ # change name of .dll in ./target/release to `points.dll`
$ # move said dll in ./target/release to top-level (where Cargo.toml is)
$ python from_rust.py
```

enjoy :D
