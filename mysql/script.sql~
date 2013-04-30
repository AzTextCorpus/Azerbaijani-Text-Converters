-- --------------------------------------------------------------------------------
-- NEATS LLC
-- 
-- 2013 April
-- Baku/Azerbaijan
-- http://neats.az
-- https://github.com/neats/Azerbaijani-Layout-Converter-for-DB
-- --------------------------------------------------------------------------------
DELIMITER $$

CREATE PROCEDURE `convert_AzLat2Unicode`(IN _table_name VARCHAR(255))
BEGIN    
    DECLARE _loop_end BOOLEAN DEFAULT FALSE; 
    DECLARE _column_name VARCHAR(200); 
    DECLARE _cursor_0 CURSOR FOR SELECT COLUMN_NAME FROM information_schema.columns WHERE TABLE_NAME=_table_name; 

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _loop_end = TRUE;
    SET SQL_SAFE_UPDATES=0;
    OPEN _cursor_0; 
        _loop_body: LOOP
            FETCH _cursor_0 INTO _column_name;
            IF _loop_end THEN 
                LEAVE _loop_body; 
            END IF; 
            
            SET @sql_for_upper = concat('UPDATE ',_table_name,' SET ',_column_name,'=REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(',_column_name,', \'ю\' ,\'ö\') , \'Б\' ,\'B\') , \'Ь\' ,\'Ğ\') , \'Т\' ,\'T\') , \'И\' ,\'İ\') , \'М\' ,\'M\') , \'С\' ,\'S\') , \'Ч\' ,\'Ç\') , \'Я\' ,\'Ə\') , \'Э\' ,\'G\') , \'Ж\' ,\'J\') , \'Д\' ,\'D\') , \'Л\' ,\'L\') , \'О\' ,\'O\') , \'Р\' ,\'R\') , \'П\' ,\'P\') , \'А\' ,\'A\') , \'В\' ,\'V\') , \'Ы\' ,\'I\') , \'Ф\' ,\'F\') , \'Ъ\' ,\'C\') , \'Х\' ,\'X\') , \'З\' ,\'Z\') , \'Щ\' ,\'H\') , \'Ш\' ,\'Ş\') , \'Г\' ,\'Q\') , \'Н\' ,\'N\') , \'Е\' ,\'E\') , \'К\' ,\'K\') , \'У\' ,\'U\') , \'Ц\' ,\'Ü\') , \'Й\' ,\'Y\') ;');
            
            PREPARE stmt_for_upper FROM @sql_for_upper;
            EXECUTE stmt_for_upper;
            DEALLOCATE PREPARE stmt_for_upper;

            SET @sql_for_lower = concat('UPDATE ',_table_name,' SET ',_column_name,'=REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(',_column_name,', \'ю\' ,\'ö\') , \'б\' ,\'b\') , \'ь\' ,\'ğ\') , \'т\' ,\'t\') , \'и\' ,\'i\') , \'м\' ,\'m\') , \'с\' ,\'s\') , \'ч\' ,\'ç\') , \'я\' ,\'ə\') , \'э\' ,\'g\') , \'ж\' ,\'j\') , \'д\' ,\'d\') , \'л\' ,\'l\') , \'о\' ,\'o\') , \'р\' ,\'r\') , \'п\' ,\'p\') , \'а\' ,\'a\') , \'в\' ,\'v\') , \'ы\' ,\'ı\') , \'ф\' ,\'f\') , \'ъ\' ,\'c\') , \'х\' ,\'x\') , \'з\' ,\'z\') , \'щ\' ,\'h\') , \'ш\' ,\'ş\') , \'г\' ,\'q\') , \'н\' ,\'n\') , \'е\' ,\'e\') , \'к\' ,\'k\') , \'у\' ,\'u\') , \'ц\' ,\'ü\') , \'й\' ,\'y\') ;');
            
            PREPARE stmt_for_lower FROM @sql_for_lower;
            EXECUTE stmt_for_lower;
            DEALLOCATE PREPARE stmt_for_lower;
                
        END LOOP _loop_body; 
    CLOSE _cursor_0; 
END
