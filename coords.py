#!/usr/bin/env python3
"""Convert between equatorial, horizontal, ecliptic coordinates."""
import math

def ra_dec_to_alt_az(ra_deg, dec_deg, lat_deg, lst_hours):
    """Equatorial to horizontal. RA in degrees, LST in hours."""
    ha = (lst_hours * 15) - ra_deg
    ha_r, dec_r, lat_r = math.radians(ha), math.radians(dec_deg), math.radians(lat_deg)
    sin_alt = math.sin(dec_r)*math.sin(lat_r) + math.cos(dec_r)*math.cos(lat_r)*math.cos(ha_r)
    alt = math.asin(sin_alt)
    cos_az = (math.sin(dec_r) - math.sin(lat_r)*math.sin(alt)) / (math.cos(lat_r)*math.cos(alt))
    cos_az = max(-1, min(1, cos_az))
    az = math.acos(cos_az)
    if math.sin(ha_r) > 0: az = 2*math.pi - az
    return math.degrees(alt), math.degrees(az)

def ecliptic_to_equatorial(lon_deg, lat_deg, obliquity=23.44):
    """Ecliptic to equatorial coordinates."""
    lon_r, lat_r, obl_r = math.radians(lon_deg), math.radians(lat_deg), math.radians(obliquity)
    ra = math.atan2(math.sin(lon_r)*math.cos(obl_r) - math.tan(lat_r)*math.sin(obl_r), math.cos(lon_r))
    dec = math.asin(math.sin(lat_r)*math.cos(obl_r) + math.cos(lat_r)*math.sin(obl_r)*math.sin(lon_r))
    return math.degrees(ra) % 360, math.degrees(dec)

if __name__ == "__main__":
    print("Celestial Coordinate Converter")
    alt, az = ra_dec_to_alt_az(101.29, -16.72, -6.9, 18.5)
    print(f"  Sirius: alt={alt:.1f}, az={az:.1f}")
    ra, dec = ecliptic_to_equatorial(120, 0)
    print(f"  Ecliptic (120,0) -> RA={ra:.1f}, Dec={dec:.1f}")\n