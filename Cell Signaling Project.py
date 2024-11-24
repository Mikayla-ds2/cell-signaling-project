def cellSignaling(signalingMolecule):
    steroidHormone = ["small", "nonpolar", "hydrophobic"] 
    peptideHormone = ["large", "polar", "hydrophilic"] #lists are characteristics from notes
#Reception
    if signalingMolecule == steroidHormone:
        def intracellularReceptor():
            print("Crossing membrane and moving to Transduction phase.")
            return
        intracellularReceptor()
    elif signalingMolecule == peptideHormone: 
        def membraneReceptor(receptorType):        
            if receptorType == 'GProtein':
                def GProtein():
                    print('Binding to GPCR.')
                    bindToGTP = True
                    if bindToGTP:
                        print('Activating G-Protein.')
                        activateGProtein = True
                        if activateGProtein:
                            print('Activating enzyme.')
                            activatedEnzyme = True
                    if activatedEnzyme == True: 
                        print("Moving to transduction phase.")
                        return
                    
            LigandReceptor = (receptorType == 'Ligand')
            if LigandReceptor:
                def Ligand(): 
                    print('Binding to ligand-gated ion channel receptor.')
                    gateOpens = True
                if gateOpens == True:  
                    print('Na+ and Ca2+ go through ion channel and go to transduction.')
                    ligandUnbinds = True
                if ligandUnbinds: 
                    gateOpens = False
                    return
    elif signalingMolecule not in [steroidHormone, peptideHormone]: 
        print('Invalid signaling molecule.')
        return
    
#Transduction
    def phosphorylationCascade(): 
        proteinActive = False
        if proteinActive == False: 
            def activateProtein(): #phosphorylation
                nonlocal proteinActive
                proteinActive = True
                print('Protein kinase transfers phosphate to ATP.')  
                proteinActive == True
            activateProtein()            
        elif proteinActive == True: 
            def deactivateProtein(): 
                nonlocal proteinActive
                proteinActive = False
                print('Protein phosphatases remove a phosphate from protein, turn off the transduction pathway, and enable protein kinase for reuse.')
            deactivateProtein()
            return
        
    def secondMessengers(): 
        secondMessenger = True
        if secondMessenger == True:
            proteinActive = True
            phosphorylationCascade()
            return
            
#Response
    transcriptionFactor = False
    def createProtein():
        transcriptionFactor = True
        print('Begins transcription and translation, then goes to the ribosome.')
    createProtein()
    return

    def inactivateProtein():
        transcriptionFactor = False
        print('Inhibits protein by competitive or noncompetitive inhibition.')
        return
    inactivateProtein()
    
cellSignaling("peptideHormone")