/// A Library about points and stuff.
extern crate libc;

#[repr(C)]
pub struct Point {
    x: libc::c_double,
    y: libc::c_double,
}

#[no_mangle]
pub extern "C" fn point_origin() -> Box<Point> {
    Box::new(Point{x: 0.0, y: 0.0})
}

#[no_mangle]
pub extern "C" fn point_new(x: libc::c_double, y: libc::c_double) -> Box<Point> {
    Box::new(Point{x: x, y: y})
}

#[no_mangle]
pub extern "C" fn point_distance(this: Box<Point>, other: Box<Point>) -> libc::c_double {
    f64::sqrt(
        f64::powi((this.x - other.x), 2) +
        f64::powi((this.y - other.y), 2)
    )
}

#[no_mangle]
pub extern "C" fn point_printer(pt: &Point) {
    println!("Point {{x: {}, y: {}}}", pt.x, pt.y)
}