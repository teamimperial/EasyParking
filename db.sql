CREATE TABLE IF NOT EXISTS `address` (
  `id_address` INT NOT NULL AUTO_INCREMENT,
  `location_name` VARCHAR(100) NOT NULL,
  `coordinates` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_address`),
  UNIQUE INDEX `id_address_UNIQUE` (`id_address` ASC),
  UNIQUE INDEX `coordinates_UNIQUE` (`coordinates` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `easyparking`.`parking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parking` (
  `id_parking` INT NOT NULL AUTO_INCREMENT,
  `id_address` INT NOT NULL,
  PRIMARY KEY (`id_parking`),
  UNIQUE INDEX `id_parking_UNIQUE` (`id_parking` ASC),
  UNIQUE INDEX `id_address_UNIQUE` (`id_address` ASC),
  CONSTRAINT `fk_dfsdfsd`
    FOREIGN KEY (`id_address`)
    REFERENCES `address` (`id_address`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `easyparking`.`line`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `line` (
  `id_line` INT NOT NULL AUTO_INCREMENT,
  `line_number` INT NOT NULL,
  `id_parking` INT NOT NULL,
  PRIMARY KEY (`id_line`),
  UNIQUE INDEX `id_line_UNIQUE` (`id_line` ASC),
  INDEX `fk_sjdsad_idx` (`id_parking` ASC),
  CONSTRAINT `fk_sjdsad`
    FOREIGN KEY (`id_parking`)
    REFERENCES `parking` (`id_parking`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `easyparking`.`place`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `place` (
  `id_place` INT NOT NULL AUTO_INCREMENT,
  `place_number` INT NOT NULL,
  `place_empty` INT NOT NULL,
  `id_line` INT NOT NULL,
  PRIMARY KEY (`id_place`),
  UNIQUE INDEX `id_place_UNIQUE` (`id_place` ASC),
  INDEX `fk_dhsdf_idx` (`id_line` ASC),
  CONSTRAINT `fk_dhsdf`
    FOREIGN KEY (`id_line`)
    REFERENCES `line` (`id_line`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
