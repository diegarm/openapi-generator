package org.openapitools.codegen.utils;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import io.swagger.v3.oas.models.media.ComposedSchema;
import io.swagger.v3.oas.models.media.Schema;

public class SchemaUtils {

    private static final Logger LOGGER = LoggerFactory.getLogger(SchemaUtils.class);
    
    public static String getNameCompose(ComposedSchema composedSchema) {
    	
    	String prefix = ""; 
    	String names = "";
    	List<Schema> schemas = null;    	
    	
    	if(composedSchema.getAllOf() != null) {
    		prefix = "AllOf";
    		schemas = composedSchema.getAllOf();
    	}
    	if(composedSchema.getOneOf() != null) {
    		prefix = "OneOf";
    		schemas = composedSchema.getOneOf();
    	}
    	if(composedSchema.getAnyOf() != null) {
    		prefix = "AnyOf";
    		schemas = composedSchema.getAnyOf();
    	}
    	
    	for (Schema schema : schemas) {
			names += getNameSchema(schema);
		}
    	
    	return prefix+names;
    	
    }
    
    public static String getNameSchema(Schema schema) {
    	
    	String nameSchema = "";
    	String refName = schema.get$ref();
    	String[] refParts = refName.split("/");
    	
    	if(refParts.length > 0) nameSchema = refParts[refParts.length-1];
    	return nameSchema;
    	
    }
	
}